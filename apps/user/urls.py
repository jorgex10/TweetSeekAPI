from django.conf.urls import url, include
from apps.user.views import APIUserList, APIUserDetail, APIUserLinkedAccounts, APIUserResults

urlpatterns = [
	url(r'^users/$', APIUserList.as_view(), name="APIUserList"),
	url(r'^users/(?P<pk>[0-9]+)/$', APIUserDetail.as_view(), name="APIUserDetail"),
  url(r'^users/(?P<pk>[0-9]+)/linked_accounts/$', APIUserLinkedAccounts.as_view(), name="APIUserLinkedAccounts"),
	url(r'^users/(?P<pk>[0-9]+)/results/$', APIUserResults.as_view(), name="APIUserResults"),
]
