from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView
from accounts.serializers import UserSerializer


class CreateUserAPIView(CreateAPIView):
    """Register user API view"""
    model = get_user_model()
    serializer_class = UserSerializer
