from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelTests(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Test Team', description='A test team')
        self.user = User.objects.create(email='test@example.com', name='Test User', team=self.team, is_superhero=True)
        self.workout = Workout.objects.create(name='Test Workout', description='A test workout', difficulty='Easy')
        self.activity = Activity.objects.create(user=self.user, type='Test Activity', duration=30, date='2025-11-04')
        self.leaderboard = Leaderboard.objects.create(user=self.user, score=100, rank=1)

    def test_user_creation(self):
        self.assertEqual(self.user.email, 'test@example.com')
        self.assertEqual(self.user.team.name, 'Test Team')

    def test_activity_creation(self):
        self.assertEqual(self.activity.type, 'Test Activity')
        self.assertEqual(self.activity.duration, 30)

    def test_leaderboard(self):
        self.assertEqual(self.leaderboard.rank, 1)
        self.assertEqual(self.leaderboard.score, 100)
