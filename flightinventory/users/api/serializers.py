from django.contrib.auth import get_user_model
from rest_framework import serializers
from flightinventory.users.models import ContactDetail
User = get_user_model()


class ContactDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactDetail
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    # contact_details = ContactDetailSerializer()
    contact_detail = ContactDetailSerializer()

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "contact_detail",
            "first_name",
            "last_name",
            "password"
        ]

    def create(self, validated_data):  # this is called when we call the .save() function
        print(validated_data)
        print("SALMAN")
        contact_info = validated_data.pop("contact_detail")
        # print(contact_info)
        # print("SALMAN")
        password = validated_data.pop("password")
        # print(password)
        # print("SALMAN")
        # print(validated_data)
        # print("SALMAN")
        user_object = super().create(validated_data)
        # print(user_object)
        # print("SALMAN")
        user_object.set_password(password)
        contact_serializer = ContactDetailSerializer(data=contact_info)  # jab bohat sarray nested hotain hain
        # print(contact_serializer)
        # print("SALMAN")
        contact_serializer.is_valid()
        # print(contact_serializer)
        # print("SALMAN")
        contact_info_obj = contact_serializer.save()
        user_object.contact_detail = contact_info_obj
        user_object.save()
        return user_object
