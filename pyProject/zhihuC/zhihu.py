import ZhihuVAPI as zhihu

self=zhihu.self
print(f'我的名字叫{self.name},目前获得了{self.voteup_count}个赞同,{self.favorited_count}个收藏,有{self.followers_count}个粉丝.提出了{self.question_count}个问题,撰写了{self.answer_count}个答案,{self.articles_count}篇文章,拥有{self.columns_count}个专栏.')