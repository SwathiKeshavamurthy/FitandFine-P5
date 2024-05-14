from rest_framework import serializers
from .models import DailyRoutine
from datetime import date

class DailyRoutineSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = DailyRoutine
        fields = [
            'id', 'owner', 'person_name', 'date', 'wake_up_time', 'breakfast_time',
            'lunch_time', 'dinner_time', 'total_calorie_intake', 'water_intake',
            'sleep_time', 'workout_minutes', 'junk', 'mood'
        ]

    def validate_date(self, value):
        """
        Check that the date is not in the future.
        """
        if value > date.today():
            raise serializers.ValidationError("The date cannot be in the future.")
        return value

    def validate_total_calorie_intake(self, value):
        if value < 0:
            raise serializers.ValidationError("Total calorie intake must be non-negative.")
        return value

    def validate_water_intake(self, value):
        if value < 0:
            raise serializers.ValidationError("Water intake must be non-negative.")
        return value

    def validate_workout_minutes(self, value):
        if value < 0:
            raise serializers.ValidationError("Workout minutes must be non-negative.")
        return value
