# _*_ coding:utf-8 _*_
from __future__ import unicode_literals
import xadmin
from xadmin import views
from .models import EmailVerifyRecord
from .models import Banner
_date_ = '2017/6/22 13:36'


#xadmin的全局设置类，固定写法
class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSetting(object):
    site_title = "宠物在线交易平台后台管理系统"
    site_footer = "宠物在线交易平台"
    menu_style = "accordion"   #把数据表列表收起


class EmailVerifyRecord_adminx(object):
    #不能继承django的models.admin，继承最底层的object
    #pass  #这里pass其实是在后台界面不现实任何一列数据，如果要显示，如同下面：
    #以下字段声明不用添加进去，只需要最后的list_display
    # code = models.CharField(max_length=25, verbose_name=u"验证码")
    # email = models.EmailField(max_length=50, verbose_name=u"邮箱")
    # send_type = models.CharField(max_length=10, choices=(("register", u"注册"), ("forget", u"忘记密码")),
    #                              verbose_name=u"验证类型")
    # send_time = models.DateTimeField(default=datetime.now, verbose_name=u"验证时间")
    #在这里如果使用元组，而且假设只有一个元素，一定要在元素后面添加逗号，例如:list_display = ('code', )
    list_display = ['code', 'email', 'send_type']   #显示

    search_fields = ['code', 'email', 'send_type']   #搜索

    list_filter = ['code', 'email', 'send_type', 'send_time']   #过滤器

xadmin.site.register(EmailVerifyRecord, EmailVerifyRecord_adminx) #EmailVerifyRecord注册到后台管理


class Banner_adminx(object):

    list_display = ['title', 'image', 'url', 'index', 'add_time']   #显示

    search_fields = ['title', 'image', 'url', 'index']   #搜索

    list_filter = ['title', 'image', 'url', 'index', 'add_time']   #过滤器

xadmin.site.register(Banner, Banner_adminx)


xadmin.site.register(views.BaseAdminView, BaseSetting)  #修改xadmin的全局设置，主题等等
xadmin.site.register(views.CommAdminView, GlobalSetting) #修改logo和管理系统页脚