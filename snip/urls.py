from django.urls import path
from . views import apiOverview, taskList, taskDetial, taskCreate, taskUpdate, taskDelete
urlpatterns = [
    path('', apiOverview, name='api-overview'),
    path('task-list/', taskList, name='task-list'),
    path('task-detail/<str:id>/', taskDetial, name='task-detail'),
    path('task-create/', taskCreate, name='task-create'),
    path('task-update/<str:id>/', taskUpdate, name='task-create'),
    path('task-delete/<str:id>/', taskDelete, name='task-delete'),
]
