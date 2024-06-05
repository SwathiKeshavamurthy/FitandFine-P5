from rest_framework import serializers
from .models import Challenge, ChallengeParticipant
from django.contrib.auth import get_user_model

User = get_user_model()

class ChallengeParticipantSerializer(serializers.ModelSerializer):
    joined_at = serializers.DateTimeField(format="%Y-%m-%d", read_only=True)

    class Meta:
        model = ChallengeParticipant
        fields = ['id', 'challenge', 'user', 'joined_at']

class ChallengeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_joined = serializers.SerializerMethodField()
    joined_at = serializers.SerializerMethodField()

    class Meta:
        model = Challenge
        fields = [
            'id', 'owner', 'title', 'description', 'start_date', 'end_date',
            'image', 'sport', 'created_at', 'updated_at', 'is_joined', 'joined_at'
        ]
        extra_kwargs = {
            'sport': {'required': True},
        }

    def get_is_joined(self, obj):
        request = self.context.get('request', None)
        if request and request.user.is_authenticated:
            return ChallengeParticipant.objects.filter(
                challenge=obj, user=request.user
            ).exists()
        return False

    def get_joined_at(self, obj):
        request = self.context.get('request', None)
        if request and request.user.is_authenticated:
            participant = ChallengeParticipant.objects.filter(
                challenge=obj, user=request.user
            ).first()
            if participant:
                return participant.joined_at
        return None

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
            raise serializers.ValidationError(
                'Image height larger than 4096px!'
            )
        if value and value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width larger than 4096px!'
            )
        return value
