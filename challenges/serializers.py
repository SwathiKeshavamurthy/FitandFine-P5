from rest_framework import serializers
from .models import Challenge, ChallengeParticipant
from django.contrib.auth import get_user_model

User = get_user_model()

class ChallengeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username') 

    class Meta:
        model = Challenge
        fields = ['id', 'owner', 'title', 'description', 'start_date', 'end_date', 'image', 'sport', 'created_at', 'updated_at']
        extra_kwargs = {
            'sport': {'required': True},
        }

    def validate_sport(self, value):
        """
        Check that the sport field is not empty and is a valid choice.
        """
        if not value:
            raise serializers.ValidationError("You must select a sport.")
        if value not in dict(self.Meta.model.SPORT_CHOICES).keys():
            raise serializers.ValidationError("Invalid choice for sport.")
        return value

    def validate_image(self, value):
        """
        Ensure image is within certain size and dimension limits if uploaded.
        """
        if value and value.size > 2 * 1024 * 1024:  # 2MB max
            raise serializers.ValidationError('Image size larger than 2MB!')
        if value and value.image.height > 4096:
            raise serializers.ValidationError('Image height larger than 4096px!')
        if value and value.image.width > 4096:
            raise serializers.ValidationError('Image width larger than 4096px!')
        return value


class ChallengeParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChallengeParticipant
        fields = '__all__'