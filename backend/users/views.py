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
