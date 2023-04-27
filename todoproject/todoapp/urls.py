from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('delete/<int:taskid>/', views.delete, name='delete'),
    path('update/<int:id>/', views.update, name='update'),
    path('cbvindex/',views.Tasklistview.as_view(),name='cbvindex'),
    path('cbvdetail/<int:pk>/',views.TaskDetailview.as_view(),name='cbvedtail'),
    path('cbvupdate/<int:pk>/',views.TaskUpdateView.as_view(),name='cbvupdate'),
    path('cbvdelete/<int:pk>/', views.TaskDeleteView.as_view(), name='cbvdelete'),

]
