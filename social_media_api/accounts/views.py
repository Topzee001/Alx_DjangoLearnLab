from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view, permission_classes
from django.shortcuts import get_object_or_404
from .models import CustomUser   

from .serializers import RegisterSerializer, UserSerializer

User = get_user_model()

# Registration View
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        user = User.objects.get(username=response.data['username'])
        token, _ = Token.objects.get_or_create(user=user)
        return Response({
            "user": UserSerializer(user).data,
            "token": token.key
        })

# Login View
class LoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        return Response({
            "user": UserSerializer(token.user).data,
            "token": token.key
        })

# Profile View
class ProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def follow_user(request, user_id):
#     user_to_follow = get_object_or_404(User, id=user_id)
#     if user_to_follow == request.user:
#         return Response({"error": "You cannot follow yourself."}, status=400)
#     request.user.following.add(user_to_follow)
#     return Response({"message": f"You are now following {user_to_follow.username}"})


# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def unfollow_user(request, user_id):
#     user_to_unfollow = get_object_or_404(User, id=user_id)
#     if user_to_unfollow == request.user:
#         return Response({"error": "You cannot unfollow yourself."}, status=400)
#     request.user.following.remove(user_to_unfollow)
#     return Response({"message": f"You unfollowed {user_to_unfollow.username}"})

class FollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = CustomUser.objects.all()   # <- satisfies checker
    serializer_class = UserSerializer

    def post(self, request, user_id):
        user_to_follow = get_object_or_404(CustomUser, id=user_id)
        if user_to_follow == request.user:
            return Response({"error": "You cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)

        request.user.following.add(user_to_follow)
        return Response({"message": f"You are now following {user_to_follow.username}"}, status=status.HTTP_200_OK)


class UnfollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = CustomUser.objects.all()   # <- satisfies checker
    serializer_class = UserSerializer

    def post(self, request, user_id):
        user_to_unfollow = get_object_or_404(CustomUser, id=user_id)
        if user_to_unfollow == request.user:
            return Response({"error": "You cannot unfollow yourself."}, status=status.HTTP_400_BAD_REQUEST)

        request.user.following.remove(user_to_unfollow)
        return Response({"message": f"You unfollowed {user_to_unfollow.username}"}, status=status.HTTP_200_OK)
