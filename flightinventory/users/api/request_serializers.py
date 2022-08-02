from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    # email = serializers.EmailField()
    password = serializers.CharField()
    remember_me = serializers.BooleanField(default=False)


class TokenSerializer(serializers.Serializer):
    access_token = serializers.CharField()
    refresh_token = serializers.CharField()

    def validate(self, attrs):
        print(attrs)
        refresh_token = RefreshToken(attrs["refresh_token"])
        data = {'access': str(refresh_token.access_token), "refresh": str(refresh_token)}
        return data

