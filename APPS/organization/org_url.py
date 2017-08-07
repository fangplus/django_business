# _*_ coding:utf-8 _*_

from django.conf.urls import url, include


from organization.views import org_list, AddUserAskView, OrgHomeView, OrgPetView, OrgDesView, OrgBossView, AddFavView, BossList, TeacherBossList


urlpatterns = [
    url(r'^list/$', org_list.as_view(), name="org_list"),
    url(r'^add_ask/$', AddUserAskView.as_view(), name="user_ask"),
    url(r'^home/(?P<org_id>\d+)$', OrgHomeView.as_view(), name="org_home"),
    url(r'^pet/(?P<org_id>\d+)$', OrgPetView.as_view(), name="org_pet"),
    url(r'^des/(?P<org_id>\d+)$', OrgDesView.as_view(), name="org_des"),
    url(r'^boss/(?P<org_id>\d+)$', OrgBossView.as_view(), name="org_boss"),

    url(r'^add_fav/(?P<org_id>\d+)$', AddFavView.as_view(), name="add_fav"),


    url(r'^boss/list/$', BossList.as_view(), name="boss_list"),
    url(r'^teacher/list/$', TeacherBossList.as_view(), name="boss_teacher_list"),


]