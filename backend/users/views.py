from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import UserProfile
from .serializers import UserProfileSerializer
@api_view(['GET'])
def health_check(request):
    return Response({
        "status": "Success",
        "message": "Django REST API is working"
    })

@api_view(['GET', 'POST'])
def user_list_create(request):

    # GET → Fetch all users
    if request.method == 'GET':
        users = UserProfile.objects.all()
        serializer = UserProfileSerializer(users, many=True)
        return Response(serializer.data)

    # POST → Create new user
    if request.method == 'POST':
        serializer = UserProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


from django.shortcuts import get_object_or_404

@api_view(['GET','PUT','PATCH','DELETE'])
def user_detail(request,pk):
    user=get_object_or_404(UserProfile,pk=pk)

    #GET -> Fetch single user
    if request.method=='GET':
        serializer=UserProfileSerializer(user)
        return Response(serializer.data)

    # PUT-> Full update
    if request.method == 'PUT':
        serializer=UserProfileSerializer(user,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    # PATCH -> Partial update
    if request.method=='PATCH':
        serializer=UserProfileSerializer(
            user,
            data=request.data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    # DELETE -> delete user
    if request.method=='DELETE':
        user.delete()
        return Response(
            {
                "message": "User deleted successfully"
            },
            status=status.HTTP_204_NO_CONTENT
        )