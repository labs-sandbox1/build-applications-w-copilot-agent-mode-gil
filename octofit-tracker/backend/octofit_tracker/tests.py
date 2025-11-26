from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class ModelTests(TestCase):
    def test_user_creation(self):
        team = Team.objects.create(name='Test Team', description='Desc')
        user = User.objects.create(name='Test User', email='test@example.com', team=team.name)
        self.assertEqual(user.name, 'Test User')
        self.assertEqual(user.team, 'Test Team')

    def test_team_creation(self):
        team = Team.objects.create(name='Test Team', description='Desc')
        self.assertEqual(team.name, 'Test Team')

    def test_activity_creation(self):
        team = Team.objects.create(name='Test Team', description='Desc')
        user = User.objects.create(name='Test User', email='test@example.com', team=team.name)
        activity = Activity.objects.create(user=user, type='Run', duration=10, date='2025-11-26')
        self.assertEqual(activity.type, 'Run')

    def test_leaderboard_creation(self):
        team = Team.objects.create(name='Test Team', description='Desc')
        leaderboard = Leaderboard.objects.create(team=team, points=50)
        self.assertEqual(leaderboard.points, 50)

    def test_workout_creation(self):
        workout = Workout.objects.create(name='Test Workout', description='Desc', difficulty='Easy')
        self.assertEqual(workout.difficulty, 'Easy')
