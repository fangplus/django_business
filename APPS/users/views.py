# _*_ coding:utf-8 _*_
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.backends import ModelBackend
from django.views.generic.base import View
from users.forms import LoginForm, ResiterForm, ForgetForm, ModifyPwdForm, UploadImageForm, UserInfoForm
from django.contrib.auth.hashers import make_password
from utils.email_send import send_register_email
from utils.mixin_utils import LoginRequiredMixin
from django.http import HttpResponse
import json
from operation.models import UserPet
# Create your views here.

from .models import UserProfile, EmailVerifyRecord


class CustomBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(username=username)
            if user.check_password(password):
                return user
        except Exception as e:
            return None


class LoginView(View):
    def get(self, request):
        return render(request, "login.html", {})

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_name = request.POST.get("username", "")
            password = request.POST.get("password", "")
            user = authenticate(username=user_name, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, "index.html")
                else:
                    return render(request, "login.html", {"msg": "用户没有激活！"})
            else:
                return render(request, "login.html", {"msg": "用户名或密码错误！"})
        else:
            return render(request, "login.html", {"login_form": login_form.errors})


class ResiterView(View):
    def get(self, request):
        register_form = ResiterForm()
        return render(request, "register.html", {'register_form': register_form})

    def post(self, request):
        register_form = ResiterForm(request.POST)
        if register_form.is_valid():
            user_name = request.POST.get("email", "")
            if UserProfile.objects.filter(email=user_name):
                return render(request, "register.html", {"register_form": register_form, "msg": "用户已经注册"})
            pass_word = request.POST.get("password", "")
            user_profile = UserProfile()
            user_profile.username = user_name
            user_profile.email = user_name
            user_profile.password = make_password(pass_word)
            user_profile.save()

            send_register_email(user_name, "register")
            return render(request, "login.html")
        else:
            return render(request, "register.html", {"register_form": register_form})


class ActiceUserView(View):
    def get(self, request, active_code):
        all_records = EmailVerifyRecord.objects.filter(code=active_code)
        if all_records:
            for record in all_records:
                email = record.email
                user = UserProfile.objects.get(email=email)
                user.is_active = True
                user.save()
        else:
            return render(request, "active_failed.html")
        return render(request, "login.html")


class ForgetPwsView(View):
    def get(self, request):
        forget_Form = ForgetForm()
        return render(request, "forgetpwd.html", {'forget_form': forget_Form})

    def post(self, request):
        forget_Form = ForgetForm(request.POST)
        if forget_Form.is_valid():
            email = request.POST.get("email", "")
            send_register_email(email, "forget")
            return render(request, "send_ok.html")
        else:
            return render(request, "forgetpwd.html", {'forget_form': forget_Form})


class ResetView(View):
    def get(self, request, active_code):
        all_records = EmailVerifyRecord.objects.filter(code=active_code)
        if all_records:
            for record in all_records:
                email = record.email
                return render(request, "password_reset.html", {"email": email})
        else:
            return render(request, "active_failed.html")
        return render(request, "login.html")


class ModifyPwdView(View):
    def post(self, request):
        modify_form = ModifyPwdForm(request.POST)
        email = request.POST.get('email', '')
        if modify_form.is_valid():
            pwd1 = request.POST.get('password1', '')
            pwd2 = request.POST.get('password2', '')
            if pwd1 != pwd2:
                return render(request, 'password_reset.html', {'email': email, 'msg': '密码不一致！'})
            user = UserProfile.objects.get(email=email)
            user.password = make_password(pwd2)
            user.save()
            return render(request, 'login.html')
        return render(request, 'password_reset.html', {'email': email, 'modify_form': modify_form})


#用户个人信息
class UserinfoView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'usercenter-info.html', {})

    def post(self, request):
        user_info_form = UserInfoForm(request.POST, instance=request.user)
        res = dict()
        if user_info_form.is_valid():
            user_info_form.save()
            res['status'] = 'success'
        else:
            res = user_info_form.errors
        return HttpResponse(json.dumps(res), content_type='application/json')


class UploadImageView(LoginRequiredMixin, View):
    def post(self, request):
        # image_form = UploadImageForm(request.POST, request.FILES)
        # if image_form.is_valid():
        #     image = image_form.cleaned_data['image']
        #     request.user.image = image
        #     request.user.save()
        image_form = UploadImageForm(request.POST, request.FILES, instance=request.user)
        res = dict()
        if image_form.is_valid():
            image_form.save()
            res['status'] = 'success'
            res['msg'] = '头像修改成功'
        else:
            res['status'] = 'fail'
            res['msg'] = '头像修改失败'
        return HttpResponse(json.dumps(res), content_type='application/json')


class UpdatePwdView(LoginRequiredMixin, View):
    #个人中心修改密码
    def post(self, request):
        modify_form = ModifyPwdForm(request.POST)
        res = dict()

        if modify_form.is_valid():
            pwd1 = request.POST.get('password1', '')
            pwd2 = request.POST.get('password2', '')
            if pwd1 != pwd2:
                res['status'] = 'fail'
                res['msg'] = '两次密码不一致'
                return HttpResponse(json.dumps(res), content_type='application/json')

            user = request.user
            user.password = make_password(pwd2)
            user.save()

            res['status'] = 'success'
            res['msg'] = '密码修改成功'
        else:
            res = modify_form.errors

        return HttpResponse(json.dumps(res), content_type='application/json')


class MyCourseView(LoginRequiredMixin, View):
    def get(self, request):
        user_pet = UserPet.objects.filter(user=request.user)
        return render(request, 'usercenter-mycourse.html', {
            'user_pet': user_pet,
        })