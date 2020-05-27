from django.shortcuts import render
from django.http import JsonResponse

# restframe work imports
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . serializers import TaskSerializer
from . models import Task


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/task-list/',
        'Detail View': 'task-detail/<str:pk>/',
        'Create': '/task-create',
        'Update': '/task-update/<str:pk>/',
        'Delete': '/task-delete/<str:pk>/'
    }
    return Response(api_urls)


@api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def taskDetial(request, id):
    tasks = Task.objects.get(pk=id)
    serializer = TaskSerializer(tasks, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def taskCreate(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def taskUpdate(request, id):
    tasks = Task.objects.get(pk=id)
    serializer = TaskSerializer(instance=tasks, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def taskDelete(request, id):
    tasks = Task.objects.get(pk=id)
    tasks.delete()
    return Response('Item Successfully deleted')
