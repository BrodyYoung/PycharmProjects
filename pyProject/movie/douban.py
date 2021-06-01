# 导入需要的库
import requests
import time
import pandas as pd
import random
from lxml import etree
from io import BytesIO
import jieba
from wordcloud import WordCloud
import numpy as np
from PIL import Image

# 为该项目创建一个类，命名nezha
# 该类有三个方法，分别是爬虫、分词、词云
class nezha():
    def __init__(self):
        # 定义session，用以加载HTML
        self.session = requests.session()
        # 定义爬虫的header,输入你浏览器上的header
        self.headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36 Edg/90.0.818.62'}
        # 豆瓣登录网址
        self.url_login = 'https://www.douban.com/login'
        #哪吒电影短评网址，注意有改动，为了动态翻页，start后加了格式化数字，短评页面有20条数据，每页增加20条
        self.url_comment = 'https://movie.douban.com/subject/26794435/comments?start=%d&limit=20&sort=new_score&status=P'

    def scrapy_(self):
        # 加载登录界面HTML
        login_request = self.session.get(self.url_login, headers=self.headers)
        # 解析HTML
        selector = etree.HTML(login_request.content)
        # 以下是登录需要填的一些信息
        post_data = {'source': 'None',  # 不需要改动
                     'redir': 'https://www.douban.com',  # 不需要改动
                     'form_email': '13613222574',  # 填账号
                     'form_password': 'yyb1415',  # 填密码
                     'login': '登录'}  # 不需要改动
        # 下面是获取验证码图片的链接
        captcha_img_url = selector.xpath('//img[@id="captcha_image"]/@src')
        # 如果有验证码，获取验证码图片，并填写图片上的验证码
        if captcha_img_url != []:
            # 获取验证码图片
            pic_request = requests.get(captcha_img_url[0])
            # 打开验证码图片
            img = Image.open(BytesIO(pic_request.content))
            img.show()
            # 填写验证码
            string = input('请输入验证码：')
            post_data['captcha-solution'] = string
            # 获取验证码匹配的字符
            captcha_id = selector.xpath('//input[@name="captcha-id"]/@value')
            # 将字符放入登录信息里
            post_data['captcha-id'] = captcha_id[0]
        # 登录
        self.session.post(self.url_login, data=post_data)
        print('已登录豆瓣')

        # 下面开始抓取短评
        # 初始化4个list用于存储信息，分别存用户名，评星，时间，评论文字
        users = []
        stars = []
        times = []
        comment_texts = []
        # 抓取500条，每页20条，这也是豆瓣给的上限
        for i in range(0, 500, 20):
            # 获取HTML
            data = self.session.get(self.url_comment % i, headers=self.headers)
            # 状态200表明页面获取成功
            print('进度', i, '条', '状态是：',data.status_code)
            # 暂停0~1秒时间，防止IP被封
            time.sleep(random.random())
            # 解析HTML
            selector = etree.HTML(data.text)
            # 用xpath获取单页所有评论
            comments = selector.xpath('//div[@class="comment"]')
            # 遍历所有评论，获取详细信息
            for comment in comments:
                # 获取用户名
                user = comment.xpath('.//h3/span[2]/a/text()')[0]
                # 获取评星
                star = comment.xpath('.//h3/span[2]/span[2]/@class')[0][7:8]
                # 获取时间
                date_time = comment.xpath('.//h3/span[2]/span[3]/@title')
                # 有的时间为空，需要判断下
                if len(date_time) != 0:
                    date_time = date_time[0]
                else:
                    date_time = None
                # 获取评论文字
                comment_text = comment.xpath('.//p/span/text()')[0].strip()
                # 添加所有信息到列表，以下相同
                users.append(user)
                stars.append(star)
                times.append(date_time)
                comment_texts.append(comment_text)
        # 用字典包装
        comment_dic = {'user': users, 'star': stars, 'time': times, 'comments': comment_texts}
        comment_df = pd.DataFrame(comment_dic)  # 转换成DataFrame格式
        comment_df.to_csv('duye_comments.csv')  # 保存数据
        comment_df['comments'].to_csv('comment.csv', index=False)  # 将评论单独再保存下来，方便分词
        print(comment_df)

    def jieba_(self):
        # 打开评论数据文件
        content = open('resrc/comment.csv', 'r', encoding='utf-8').read()
        # jieba分词
        word_list = jieba.cut(content)
        # 添加自定义词，该片经典台词‘我命由我不由天’必须加进去
        # with open('自定义词.txt') as f:
        #     jieba.load_userdict(f)
        # 新建列表，收集词语
        word = []
        # 去掉一些无意义的词和符号，我这里自己整理了停用词库
        # for i in word_list:
        #     with open('停用词库.txt') as f:
        #         meaningless_file = f.read().splitlines()
        #         f.close()
        #     if i not in meaningless_file:
        #         word.append(i.replace(' ', ''))
        # 全局变量，方便词云使用
        global word_cloud
        # 用逗号隔开词语
        word_cloud = '，'.join(word)
        print(word_cloud)

    def word_cloud_(self):
        # 打开你喜欢的词云展现背景图，这里选用哪吒电影里的图片
        cloud_mask = np.array(Image.open('resrc/nezha.jpg'))
        # 定义词云的一些属性
        wc = WordCloud(
            background_color="white",  # 背景图分割颜色为白色
            mask=cloud_mask,  # 背景图样
            max_words=300,  # 显示最大词数
            font_path='./fonts/simhei.ttf',  # 显示中文
            min_font_size=5,  # 最小尺寸
            max_font_size=100,  # 最大尺寸
            width=400  # 图幅宽度
        )
        # 使用全局变量，刚刚分出来的词
        global word_cloud
        # 词云函数
        x = wc.generate(word_cloud)
        # 生成词云图片
        image = x.to_image()
        # 展示词云图片
        image.show()
        # 保存词云图片
        wc.to_file('pic.png')

# 创建类对象
nezha = nezha()
# 抓取豆瓣短评
nezha.scrapy_()
# 使用jieba对短评进行分词
nezha.jieba_()
# 使用wordcloud展示词云
nezha.word_cloud_()