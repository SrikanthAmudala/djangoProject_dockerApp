from __future__ import unicode_literals

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Q
# Create your views here.
from .models import Task
from .serializers import TaskSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


@api_view(["POST"])
def sampleAPI(request):
    try:
        result = {"result": "this is working"}
        return Response(result, status=status.HTTP_200_OK)
    except Exception as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
# @authentication_classes([TokenAuthentication])
# @permission_classes([IsAuthenticated])
def taskList(request):
    """
    :param request:
    :return: by default orders by id, if provided a field it will do so with that
    """
    try:

        userID = request.data.get("userID", None)
        title = request.data.get("title", None)
        desc = request.data.get("desc", None)
        stat = request.data.get("status", None)
        taskDueDate = request.data.get("taskDueDate", None)
        sortby = request.data.get("sortby", None)
        if sortby:
            qs = Task.objects.all().order_by(sortby)
        else:
            qs = Task.objects.all().order_by('-id')

        if userID:
            qs = qs.filter(Q(userID__exact=userID))

        if title:
            qs = qs.filter(Q(title__exact=title))

        if desc:
            qs = qs.filter(Q(desc__exact=desc))

        if stat:
            qs = qs.filter(Q(status__exact=stat))

        if taskDueDate:
            qs = qs.filter(Q(taskDueDate__exact=taskDueDate))

        serializer = TaskSerializer(qs, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


    except Exception as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def taskCreate(request):
    # {'desc': 'Sample task 3', 'taskDueDate': '2020-05-23', 'title': 'Task 3', 'status': 'DONE', 'userID': 'Sunny'}
    print("data: ", request.data)
    serializer = TaskSerializer(data=request.data)
    print("task valid: ", serializer.is_valid())
    if serializer.is_valid():
        serializer.save()
    # Task.save(serializer.data)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["POST"])
def taskUpdate(request):
    task = Task.objects.get(id=request.data.get('id'))
    serializer = TaskSerializer(instance=task, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["POST"])
def taskDelete(request):
    try:
        id = request.data.get("id", None)
        if not id:
            raise ValueError({"error": "id is empty"})

        task = Task.objects.get(id=id)
        task.delete()
        return Response(True, status=status.HTTP_200_OK)

    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)
