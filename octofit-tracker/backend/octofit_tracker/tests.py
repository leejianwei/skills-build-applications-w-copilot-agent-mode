from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class UserModelTest(TestCase):
    def test_create_user(self):
        team = Team.objects.create(name='Marvel')
        user = User.objects.create(name='Iron Man', email='ironman@marvel.com', team=team)
        self.assertEqual(user.name, 'Iron Man')
        self.assertEqual(user.team.name, 'Marvel')

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name='DC')
        self.assertEqual(team.name, 'DC')

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        team = Team.objects.create(name='Marvel')
        user = User.objects.create(name='Hulk', email='hulk@marvel.com', team=team)
        activity = Activity.objects.create(user=user, type='Running', duration=30, date='2025-09-03')
        self.assertEqual(activity.type, 'Running')

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        team = Team.objects.create(name='Marvel')
        workout = Workout.objects.create(name='Pushups', description='Do 20 pushups')
        workout.suggested_for.add(team)
        self.assertIn(team, workout.suggested_for.all())

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        team = Team.objects.create(name='Marvel')
        leaderboard = Leaderboard.objects.create(team=team, points=100)
        self.assertEqual(leaderboard.points, 100)
