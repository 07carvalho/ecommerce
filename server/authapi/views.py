from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import UserRegisterSerializer, UserLoginSerializer


class UserCreate(generics.CreateAPIView):
    """Create a new User."""
    description = 'This route is used to create a new User.'
    serializer_class = UserRegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLogin(generics.RetrieveAPIView):
    """Login a User."""
    description = 'This route is used to login a User.'
    serializer_class = UserLoginSerializer

    def put(self, request, *args, **kwargs):
        serializer = UserLoginSerializer(data=request.data, context={'request': request})
        # if serializer.is_valid():
        print("VALId")
        serializer.login()
        return Response(serializer.data, status=status.HTTP_200_OK)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
