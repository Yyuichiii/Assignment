from rest_framework import serializers
from .models import MyUser


class UserRegistrationSerializers(serializers.ModelSerializer):
    password2=serializers.CharField(style={'input_type':'password'},write_only=True)
    Code=serializers.CharField(max_length=6,allow_blank=True,required=False)
    class Meta:
        model=MyUser
        fields=['email','name','password','password2','Code']
        extra_kwargs={'password':{'write_only':True}}

    # Valdiate password and password 2
    def validate(self,attrs):
        password=attrs.get('password')
        password2=attrs.get('password2')
        

        if password!=password2:
            raise serializers.ValidationError("Password and Confirm Password does'nt match")
        
        return attrs
    

    def create(self, validated_data):
        email=validated_data.get('email')
        name=validated_data.get('name')
        password=validated_data.get('password')
        Code=validated_data.get('Code')
        if Code:
            try:
                referred_user=MyUser.objects.get(referral_code=Code)
                referred_user.points+=1
                referred_user.save()
            except:
                raise serializers.ValidationError("The entered referral code is not valid")
        return MyUser.objects.create_user(email,name,password)