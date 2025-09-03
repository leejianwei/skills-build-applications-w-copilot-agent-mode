from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Activity, Team
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the database with test data for all collections.'

    def handle(self, *args, **options):
        # Clear existing data
        User.objects.all().delete()
        Activity.objects.all().delete()
        Team.objects.all().delete()

        # Create Teams
        team1, _ = Team.objects.get_or_create(name='OctoWarriors')
        team2, _ = Team.objects.get_or_create(name='FitSquad')

        # Create Users
        user1, _ = User.objects.get_or_create(email='alice@example.com', defaults={'name': 'Alice', 'team': team1})
        user2, _ = User.objects.get_or_create(email='bob@example.com', defaults={'name': 'Bob', 'team': team1})
        user3, _ = User.objects.get_or_create(email='carol@example.com', defaults={'name': 'Carol', 'team': team2})

        # Create Activities
        Activity.objects.create(user=user1, type='Running', duration=30, date=timezone.now())
        Activity.objects.create(user=user2, type='Cycling', duration=45, date=timezone.now())
        Activity.objects.create(user=user3, type='Swimming', duration=60, date=timezone.now())

        self.stdout.write(self.style.SUCCESS('Test data populated successfully.'))