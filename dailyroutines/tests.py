from django.test import TestCase
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from .models import DailyRoutine
from datetime import date, time, timedelta

User = get_user_model()

class DailyRoutineTestCase(TestCase):
    def setUp(self):
        # Create a user for the test case
        self.user = User.objects.create_user(username='testuser', password='testpass')

        # Create a daily routine for today
        self.daily_routine = DailyRoutine.objects.create(
            owner=self.user,
            person_name="Test User",
            date=date.today(),
            wake_up_time=time(7, 0),
            breakfast_time=time(8, 0),
            lunch_time=time(13, 0),
            dinner_time=time(19, 0),
            total_calorie_intake=2000,
            water_intake=2000,
            sleep_time=time(23, 0),
            workout_minutes=60,
            junk=False,
            mood='happy'
        )

    def test_daily_routine_creation(self):
        """
        Test the creation of a daily routine and its attributes.
        """
        self.assertEqual(self.daily_routine.owner.username, 'testuser')
        self.assertEqual(self.daily_routine.mood, 'happy')

    def test_date_not_in_future(self):
        """
        Ensure that the date cannot be set in the future.
        """
        future_date = date.today() + timedelta(days=1)
        with self.assertRaises(ValidationError):
            DailyRoutine.objects.create(
                owner=self.user,
                person_name="Test User",
                date=future_date,
                wake_up_time=time(7, 0),
                breakfast_time=time(8, 0),
                lunch_time=time(13, 0),
                dinner_time=time(19, 0),
                total_calorie_intake=1500,
                water_intake=1500,
                sleep_time=time(23, 0),
                workout_minutes=30,
                junk=False,
                mood='energetic'
            ).full_clean()

    def test_update_routine_mood(self):
        """
        Test updating the mood of a daily routine.
        """
        self.daily_routine.mood = 'tired'
        self.daily_routine.save()
        updated_routine = DailyRoutine.objects.get(id=self.daily_routine.id)
        self.assertEqual(updated_routine.mood, 'tired')

    def test_profile_link(self):
        """
        Test if the daily routine correctly links to a user's profile.
        """
        self.assertEqual(self.daily_routine.owner, self.user)

    def test_realistic_water_intake(self):
        """
        Test for realistic water intake values.
        """
        self.daily_routine.water_intake = 20001
        with self.assertRaises(ValidationError):
            self.daily_routine.full_clean()

    def test_default_junk(self):
        """
        Test the default setting for junk food consumption.
        """
        new_routine = DailyRoutine(
            owner=self.user,
            date=date.today(),
            wake_up_time=time(7, 0),
            breakfast_time=time(8, 0),
            lunch_time=time(13, 0),
            dinner_time=time(19, 0),
            total_calorie_intake=2000,
            water_intake=1500,
            sleep_time=time(23, 0),
            workout_minutes=45,
            mood='happy'
        )
        self.assertFalse(new_routine.junk) 
