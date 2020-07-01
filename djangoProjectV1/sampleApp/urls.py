from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^toAPI/', views.sampleAPI),
    url(r'^addTODO/', views.taskCreate),
    # url(r'^deleteTODO/<str:pk>/', views.taskDelete),
    url(r'^deleteTODO/', views.taskDelete),
    url(r'^updateTODO/', views.taskUpdate),
    url(r'^listallTODO/', views.taskList),
]
