from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from .models import CustomUser, GroupOfUser
from .serializers import UserSerializer, GroupSerializer
from rest_framework import status


# Views for printing all data
@api_view(['GET'])
def getUsers(request):
    users = CustomUser.objects.all().select_related()
    # data = CustomUser.objects.select_related('group').all()
    # print(data)
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getGroups(request):
    groups = GroupOfUser.objects.all()
    serializer = GroupSerializer(groups, many=True)
    return Response(serializer.data)


# Views for adding data
@api_view(['POST'])
def addUser(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def addGroup(request):
    serializer = GroupSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


# Views for updating data
@api_view(['POST'])
def editUser(request, pk):
    user = CustomUser.objects.get(id=pk)
    serializer = UserSerializer(instance=user, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def editGroup(request, pk):
    group = GroupOfUser.objects.get(id=pk)
    serializer = GroupSerializer(instance=group, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


# Views for deleting data
@api_view(['DELETE'])
def deleteUser(request, pk):
    user = CustomUser.objects.get(id=pk)
    user.delete()
    return Response("User was successfully deleted")

@api_view(['DELETE'])
def deleteGroup(request, pk):
    group = GroupOfUser.objects.get(id=pk)
    users = CustomUser.objects.all()
    for user in users:
        print("user group id: ")
        print(user.group.id)
        print("group id: ")
        print(group.id)
        if user.group.id == group.id:
            return Response("Group cannot be deleted")
        else:
            group.delete()
            return Response("Group was successfully deleted")



# Views for filtering the data

@api_view(['GET'])
def filterData(request):
    data = request.data
    if request.data['table'] == 'Users':  # table in request
        if data['filter'][0]['field'] == "username":  # field in request
            if data['filter'][0]['filter_function'] == "like":  # function in request
                users = CustomUser.objects.filter(
                    username__contains=data['filter'][0]['filter_input'])  # filter_input in request
                serializer = UserSerializer(users, many=True)
                return Response(serializer.data)
        elif data['filter'][0]['field'] == "created":
            if data['filter'][0]['filter_function'] == "biggerThanDate":
                users = CustomUser.objects.filter(created__gte=data['filter'][0]['filter_input'])
                serializer = UserSerializer(users, many=True)
                return Response(serializer.data)
            elif data['filter'][0]['filter_function'] == "lessThanDate":
                users = CustomUser.objects.filter(created__lte=data['filter'][0]['filter_input'])
                serializer = UserSerializer(users, many=True)
                return Response(serializer.data)
        elif data['filter'][0]['field'] == "group":
            if data['filter'][0]['filter_function'] == "usersInGroup":
                users = CustomUser.objects.filter(group=data['filter'][0]['filter_input'])
                serializer = UserSerializer(users, many=True)
                return Response(serializer.data)

    elif data['table'] == 'Groups':
        if data['filter'][0]['field'] == 'id':
            if data['filter'][0]['filter_function'] == "groupsWithBiggerID":
                groups = GroupOfUser.objects.filter(id__gte=data['filter'][0]['filter_input'])
                serializer = GroupSerializer(groups, many=True)
            elif data['filter'][0]['filter_function'] == "groupsWithLessID":
                groups = GroupOfUser.objects.filter(id__lte=data['filter'][0]['filter_input'])
                serializer = GroupSerializer(groups, many=True)
            return Response(serializer.data)
        elif data['filter'][0]['field'] == 'name':
            if data['filter'][0]['filter_function'] == "like":
                groups = GroupOfUser.objects.filter(name__contains=data['filter'][0]['filter_input'])
                serializer = GroupSerializer(groups, many=True)
                return Response(serializer.data)
        elif data['filter'][0]['field'] == 'description':
            if data['filter'][0]['filter_function'] == "like":
                groups = GroupOfUser.objects.filter(description__contains=data['filter'][0]['filter_input'])
                serializer = GroupSerializer(groups, many=True)
                return Response(serializer.data)

    message = {'detail': "Error. HTTP_400_BAD_REQUEST"}
    return Response(message, status=status.HTTP_400_BAD_REQUEST)