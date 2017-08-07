# _*_ coding:utf-8 _*_
from django.conf.urls import url, include


from organization.views import org_list, AddUserAskView, OrgHomeView, OrgPetView, OrgDesView, OrgBossView, AddFavView
from .views import PetList, CourseList, PetDetailView

urlpatterns = [
    #课程列表页
    url(r'^list/$', PetList.as_view(), name="pet_list"),
    url(r'^list/$', CourseList.as_view(), name="course_list"),

    url(r'^detail/(?P<pet_id>.*)/$', PetDetailView.as_view(), name='pet_detai'),
]