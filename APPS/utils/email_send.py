# _*_ coding:utf-8 _*_

from users.models import EmailVerifyRecord
from random import Random
from django.core.mail import send_mail
from Djangobusiness.settings import EMAIL_FROM


def generate_random_str(randomlength=16):
    str = ''
    chars = 'abcdefghijklmnopqrstuvwxyz1234567890'
    length = len(chars)-1
    for i in range(randomlength):
        str += chars[Random().randint(0, length)]
    #str = ''.join(Random().randint(0, length) for _ in range(randomlength))
    return str


def send_register_email(email, send_type="register"):
    email_record = EmailVerifyRecord()
    code = generate_random_str(16)
    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()
    if send_type == "register":
        email_title = "宠物在线网注册激活连接"
        email_body = "请点击下列链接激活你的帐号：http://127.0.0.1:8000/active/{0}".format(code)
        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass
    elif send_type == "forget":
        email_title = "宠物在线网修改密码激活连接"
        email_body = "请点击下列链接修改你的帐号：http://127.0.0.1:8000/reset/{0}".format(code)
        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass







