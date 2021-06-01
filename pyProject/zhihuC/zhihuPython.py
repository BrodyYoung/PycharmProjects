from zhihu_oauth import ZhihuClient
from zhihu_oauth.exception import NeedCaptchaException

client = ZhihuClient()

try:
    # client.login('+8613613222574', 'yyb1415.')
    client.login_in_terminal('+8613613222574', 'yyb1415.')
except NeedCaptchaException:
    # 保存验证码并提示输入，重新登录
    with open('resrc/a.gif', 'wb') as f:
        f.write(client.get_captcha())
    captcha = input('please input captcha:')
    client.login('email_or_phone', 'password', captcha)