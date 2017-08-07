# _*_ coding:utf-8 _*_
import json
from django.shortcuts import render
from django.views.generic import View
from .models import pet_organization, City, pet_boss
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from .form import UserAskForm
from pets.models import pet_organization
from operation.models import UserFavorite
from django.db.models import Q
# Create your views here.


class org_list(View):
    def get(self, request):
        #宠物店
        all_orgs = pet_organization.objects.all()

        #城市
        all_citys = City.objects.all()

        #热门店铺筛选
        hot_org = all_orgs.order_by("-click_nums")[:3]

        search_keywords = request.GET.get('keywords', "")
        if search_keywords:
            all_orgs = all_orgs.filter(Q(name__icontains=search_keywords) | Q(des__icontains=search_keywords))

        city_id = request.GET.get('city', "")
        if city_id:
            all_orgs = all_orgs.filter(city_id=int(city_id))

        catgory = request.GET.get('ct', "")
        if catgory:
            all_orgs = all_orgs.filter(catgory=catgory)

        sort = request.GET.get("sort", "")
        if sort:
            if sort == "favorite_nums":
                all_orgs = all_orgs.order_by("-favorite_nums")
            elif sort == "click_nums":
                all_orgs = all_orgs.order_by("-click_nums")

        all_nums = all_orgs.count()

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        # objects = ['john', 'edward', 'josh', 'frank']

        # Provide Paginator with the request object for complete querystring generation

        p = Paginator(all_orgs, 4, request=request) #对店铺进行分页

        orgs = p.page(page)

        return render(request, "org-list.html", {
            "all_orgs": orgs,
            "all_citys": all_citys,
            "all_nums": all_nums,
            "city_id": city_id,
            "catgory": catgory,
            "hot_org": hot_org,
            "sort": sort
        })


class AddUserAskView(View):
    #用户宠物咨询
    def post(self, request):
        useraskform = UserAskForm(request.POST)
        res = dict()
        if useraskform.is_valid():
            useraskform.save(commit=True)
            res['status'] = 'success'
        else:
            res['status'] = 'fail'
            res['msg'] = '添加出错'
        return HttpResponse(json.dumps(res), content_type='application/json')


class OrgHomeView(View):
    #店铺首页
    def get(self, request, org_id):
        current_page = "home"
        pet_org = pet_organization.objects.get(id=int(org_id))
        all_pet = pet_org.petinformation_set.all()
        all_boss = pet_org.pet_boss_set.all()
        return render(request, 'org-detail-homepage.html', {
            "all_pet": all_pet,
            "all_boss": all_boss,
            "pet_org": pet_org,
            "current_page": current_page,
        })


class OrgPetView(View):
    #店铺宠物
    def get(self, request, org_id):
        current_page = "pet"
        pet_org = pet_organization.objects.get(id=int(org_id))
        all_pet = pet_org.petinformation_set.all()
        return render(request, 'org-detail-course.html', {
            "all_pet": all_pet,
            "pet_org": pet_org,
            "current_page": current_page,
        })


class OrgDesView(View):
    #店铺介绍
    def get(self, request, org_id):
        current_page = "org"
        pet_org = pet_organization.objects.get(id=int(org_id))
        return render(request, 'org-detail-desc.html', {
            "pet_org": pet_org,
            "current_page": current_page,
        })


class OrgBossView(View):
    #店铺老板介绍
    def get(self, request, org_id):
        current_page = "boss"
        pet_org = pet_organization.objects.get(id=int(org_id))
        all_boss = pet_org.pet_boss_set.all()
        return render(request, 'org-detail-teachers.html', {
            "pet_org": pet_org,
            "current_page": current_page,
            "all_boss": all_boss,
        })


class AddFavView(View):
    #用户收藏
    def post(self, request):
        fav_id = request.POST.get('fav_id', 0)
        fav_type = request.POST.get('fav_type', 0)
        res = dict()
        #判断用户登录操作
        if not request.user.is_authenticated():
            return HttpResponse("{'status': 'fail', 'mas': '用户未登录'}", content_type='application/json')
        else:
            exist_record = UserFavorite.objects.filter(user=request, fav_id=int(fav_id), fav_type=fav_type)
            #判断收藏是否存在
            if exist_record:
                exist_record.delete()
                return HttpResponse("{'status': 'success', 'mas': '已取消收藏'}", content_type='application/json')
            else:
                user_fav = UserFavorite()
                if int(fav_id) > 0 and int(fav_type) > 0:
                    user_fav.fav_id = int(fav_id)
                    user_fav.fav_type = int(fav_type)
                    user_fav.save()
                    return HttpResponse("{'status': 'success', 'mas': '已收藏'}", content_type='application/json')
                else:
                    return HttpResponse("{'status': 'fail', 'mas': '收藏失败'}", content_type='application/json')


class BossList(View):
    def get(self, request):
        all_boss = pet_boss.objects.all()

        sort = request.GET.get("sort", "")
        if sort:
            if sort == "favorite_nums":
                all_boss = all_boss.order_by("-favorite_nums")
            elif sort == "click_nums":
                all_boss = all_boss.order_by("-click_nums")

        all_nums = all_boss.count()

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        # objects = ['john', 'edward', 'josh', 'frank']

        # Provide Paginator with the request object for complete querystring generation

        p = Paginator(all_boss, 4, request=request)  # 对店铺进行分页

        boss = p.page(page)

        return render(request, 'teachers-list.html', {
            "all_boss": boss,
            "sort": sort,
            "all_nums": all_nums,
        })


class TeacherBossList(View):
    def get(self, request):
        all_boss = pet_boss.objects.all()

        sort = request.GET.get("sort", "")
        if sort:
            if sort == "favorite_nums":
                all_boss = all_boss.order_by("-favorite_nums")
            elif sort == "click_nums":
                all_boss = all_boss.order_by("-click_nums")

        search_keywords = request.GET.get('keywords', "")
        if search_keywords:
            all_boss = all_boss.filter(Q(name__icontains=search_keywords) | Q(work_org__name__icontains=search_keywords))

        all_nums = all_boss.count()

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        # objects = ['john', 'edward', 'josh', 'frank']

        # Provide Paginator with the request object for complete querystring generation

        p = Paginator(all_boss, 4, request=request)  # 对店铺进行分页

        boss = p.page(page)

        return render(request, 'teachers-list.html', {
            "all_boss": boss,
            "sort": sort,
            "all_nums": all_nums,
        })