from django.conf.urls import url

from . import views

urlpatterns = [
               url(r'^(?P<item_id>[0-9]+)/detail/$', views.update_task, name='update_task'),
               url(r'^$',
                   views.add_task, name='add_task'),

               url(r'^todolist/deleteTask/(?P<item_id>\w+)/$',
                   views.deleteTask,name='deleteTask'),

               url(r'^todolist/markIt/(?P<item_id>\w+)/$',
                   views.markIt,name='markIt'),
               ]
