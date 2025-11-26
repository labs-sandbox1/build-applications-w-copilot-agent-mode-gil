from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='Marvel', description='Marvel Superheroes')
        dc = Team.objects.create(name='DC', description='DC Superheroes')

        # Users
        users = [
            User(name='Spider-Man', email='spiderman@marvel.com', team=marvel.name),
            User(name='Iron Man', email='ironman@marvel.com', team=marvel.name),
            User(name='Wonder Woman', email='wonderwoman@dc.com', team=dc.name),
            User(name='Batman', email='batman@dc.com', team=dc.name),
        ]
        for user in users:
            user.save()

        # Activities
        Activity.objects.create(user=users[0], type='Running', duration=30, date='2025-11-25')
        Activity.objects.create(user=users[1], type='Cycling', duration=45, date='2025-11-25')
        Activity.objects.create(user=users[2], type='Swimming', duration=60, date='2025-11-25')
        Activity.objects.create(user=users[3], type='Yoga', duration=50, date='2025-11-25')

        # Leaderboard
        Leaderboard.objects.create(team=marvel, points=100)
        Leaderboard.objects.create(team=dc, points=120)

        # Workouts
        Workout.objects.create(name='Hero HIIT', description='High intensity for heroes', difficulty='Hard')
        Workout.objects.create(name='Power Yoga', description='Yoga for super strength', difficulty='Medium')

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data'))
