# _*_ coding:utf-8 _*_
from django.shortcuts import render
from django.views.generic.base import View
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

# Create your views here.
from pets.models import PetInformation

class PetList(View):
    def get(self, request):
        all_pet = PetInformation.objects.all()

        #宠物搜索
        search_keywords = request.GET.get('keywords', "")
        if search_keywords:
            all_pet = all_pet.filter(Q(name__icontains=search_keywords)|Q(des__icontains=search_keywords)|Q(detail__icontains=search_keywords))

        sort = request.GET.get("sort", "")
        if sort:
            if sort == "buy_people_num":
                all_pet = all_pet.order_by("-buy_people_num")
            elif sort == "price":
                all_pet = all_pet.order_by("-price")

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        # objects = ['john', 'edward', 'josh', 'frank']

        # Provide Paginator with the request object for complete querystring generation

        p = Paginator(all_pet, 3, request=request) #对店铺进行分页

        pet = p.page(page)

        return render(request, 'course-list.html', {
            "all_pet": pet,
            "sort": sort,
        })


class CourseList(View):
    def get(self, request):
        all_pet = PetInformation.objects.all()

        #宠物搜索
        search_keywords = request.GET.get('keywords', "")
        if search_keywords:
            all_pet = all_pet.filter(Q(name__icontains=search_keywords)|Q(des__icontains=search_keywords)|Q(detail__icontains=search_keywords))

        sort = request.GET.get("sort", "")
        if sort:
            if sort == "buy_people_num":
                all_pet = all_pet.order_by("-buy_people_num")
            elif sort == "price":
                all_pet = all_pet.order_by("-price")

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        # objects = ['john', 'edward', 'josh', 'frank']

        # Provide Paginator with the request object for complete querystring generation

        p = Paginator(all_pet, 3, request=request) #对店铺进行分页

        pet = p.page(page)

        return render(request, 'course-list.html', {
            "all_pet": pet,
            "sort": sort,
        })


class PetDetailView(View):

    def get(self, request, pet_id):
        pet = PetInformation.objects.get(id=int(pet_id))
        return render(request, 'course-detail.html', {
            "pet": pet,
        })