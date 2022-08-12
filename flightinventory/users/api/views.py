import logging
from django.contrib.auth import authenticate
from rest_framework import permissions
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
from rest_framework_simplejwt.tokens import RefreshToken

from flightinventory.users.api.request_serializers import SearchingUserSerializer
from flightinventory.users.api.request_serializers import UserLoginSerializer, TokenSerializer
from flightinventory.users.api.serializers import UserSerializer
from flightinventory.users.models import User


class UserViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = "username"

    def get_queryset(self, *args, **kwargs):
        assert isinstance(self.request.user.id, int)
        return self.queryset.filter(id=self.request.user.id)

    @action(detail=False)
    def me(self, request):
        serializer = UserSerializer(request.user, context={"request": request})
        return Response(status=status.HTTP_200_OK, data=serializer.data)


class RefreshTokenGetter(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = TokenSerializer(data=request.data)
        logging.info(request.data)
        logging.info(serializer)
        try:
            logging.info("in try")
            serializer.is_valid(raise_exception=True)
            return Response(serializer.validated_data, status=status.HTTP_200_OK)
        except Exception as exc:
            logging.exception("Some error occurred", exc)
            return Response({}, status=status.HTTP_401_UNAUTHORIZED)


class UserLoginAPI(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        request_data = UserLoginSerializer(data=request.data)  # initialize request with the object of serializer
        request_data.is_valid(raise_exception=True)
        username = request_data.validated_data.get("username")
        email = request_data.validated_data.get("email")
        password = request_data.validated_data.get("password")
        logging.info(request_data.validated_data)
        user = authenticate(username=username, email=email, password=password)

        if not user:
            return Response(
                data="Unable to login",
                status=status.HTTP_401_UNAUTHORIZED,
            )

        refresh_token = RefreshToken.for_user(user)

        return Response(
            data={
                "access": str(refresh_token.access_token),
                "refresh": str(refresh_token),
                "user": UserSerializer(user).data,
                "message": "You are logged in",
            },
            status=status.HTTP_200_OK,
        )


class UserSignupAPI(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        user = UserSerializer(data=request.data)
        try:
            user.is_valid(raise_exception=True)
            user.save()
            return Response(data={"message": "User is created"}, status=status.HTTP_200_OK)
        except Exception as err:
            logging.exception("Error occured while ")
            return Response(data={'message': "Enter correct data"}, status=status.HTTP_400_BAD_REQUEST)


class UserSearchAPI(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        user = SearchingUserSerializer(data=request.data, many=True)
        try:
            user.is_valid(raise_exception=True)
            valid_user = user.validated_data
            logging.info(valid_user)
            usernames = [val['username'] for val in valid_user]
            logging.info(usernames)
            users = User.objects.filter(username__in=usernames)
            return Response(
                data={
                    "message": f"{users} is in the database",
                    "user": UserSerializer(users, many=True).data
                },
                status=status.HTTP_200_OK)
        except Exception as error:
            logging.exception(f"Error = {error}")
            return Response(data={"message": "Invalid data entered"}, status=status.HTTP_400_BAD_REQUEST)
