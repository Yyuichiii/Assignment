from rest_framework import serializers
from .models import MyUser

class UserRegistrationSerializers(serializers.ModelSerializer):
    """
    Serializer for user registration.

    Attributes:
        password2 (serializers.CharField): Confirmation password field.
        Code (serializers.CharField): Referral code field.
    """

    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    Code = serializers.CharField(max_length=6, allow_blank=True, required=False)

    class Meta:
        """
        Meta class for model and fields specification.
        """

        model = MyUser
        fields = ['email', 'name', 'password', 'password2', 'Code']
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, attrs):
        """
        Validates password match.
        """

        password = attrs.get('password')
        password2 = attrs.get('password2')

        if password != password2:
            raise serializers.ValidationError("Passwords don't match")

        return attrs

    def create(self, validated_data):
        """
        Creates a new user instance and rewards referred users with points.
        """

        email = validated_data.get('email')
        name = validated_data.get('name')
        password = validated_data.get('password')
        Code = validated_data.get('Code')
        new_user=MyUser.objects.create_user(email, name, password)

        if Code:
            try:
                referred= MyUser.objects.get(referral_code=Code)
                referred.points += 1
                referred.referred_user.add(new_user)
                referred.save()

            except MyUser.DoesNotExist:
                raise serializers.ValidationError("Invalid referral code")

        return new_user
