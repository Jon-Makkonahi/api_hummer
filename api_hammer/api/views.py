from django.core.mail import send_mail

from random import randint

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import (
    AuthUserSerializer,
    UserSerializer,
    ActivitionInviteUserSerializer
)
from users.models import User


@api_view(['POST'])
def get_code(request):
    code = randint(999, 10000)
    if request.method == 'POST':
        send_mail(
        'Ваш код для регистрации',
        f'Здравствуйте, ваш код {code}',
        'best_company@gmail.com',
        ['users@gmail.com'],
        fail_silently=False,
    )
        return Response({'password': f'Ваш код - {code}!'})


@api_view(['POST'])
def authencation(request):
    if request.method == 'POST':
        serializer = AuthUserSerializer(data=request.data)
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


@api_view(['GET'])
def get_list(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_profile(request, phone):
    if request.method == 'GET':
        user = User.objects.get(phone=phone)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PATCH'])
def edit_profile(request, phone):
    if request.method == 'PATCH':
        if 'invite_code' not in request.data:
            return Response(
                ['invite_code: Не введен'],
                status=status.HTTP_400_BAD_REQUEST
            )
        user = User.objects.get(phone=phone)
        serializer = ActivitionInviteUserSerializer(
            user,
            data=request.data,
            partial=True
        )
        if serializer.is_valid(raise_exception=True):
            if request.data["activation"] > 1:
                return Response(
                    [
                        f'Нельзя еще раз использовать invite-{serializer.data}'
                ],
                    status=status.HTTP_400_BAD_REQUEST
            )
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_206_PARTIAL_CONTENT
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    if request.method == 'GET':
        user = User.objects.get(phone=phone)
        serializer = ActivitionInviteUserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)