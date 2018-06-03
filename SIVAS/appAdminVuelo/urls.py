
from django.conf.urls import url
from appAdminVuelo import views
from appAdminVuelo.views import *

urlpatterns = [
    url(r'^linea_list/', linea_list.as_view(), name='linea_list'),
    url(r'^lineaCreate/', lineaCreate, name='lineaCreate'),
    url(r'^lineaUpdate/(?P<id_linea>[\w-]+)/$', lineaUpdate, name='lineaUpdate'),
    url(r'^lineaDelete/(?P<pk>[\w-]+)/$', lineaDelete.as_view(), name='lineaDelete'),
    url(r'^lineaDetail(?P<pk>[\w-]+)/$', lineaDetail, name='lineaDetail'),

#url(r'^(?P<pk>\d+)$', CourseDetail.as_view(), name='detail'),

]

