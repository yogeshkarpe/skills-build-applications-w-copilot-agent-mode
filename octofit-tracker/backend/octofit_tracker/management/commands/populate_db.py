from django.core.management.base import BaseCommand
from octofit_tracker.models import Team, User, Activity, Workout, Leaderboard
from datetime import date

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data in correct order and avoid holding instances in memory
        Leaderboard.objects.all().delete()
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel', description='Marvel superheroes')
        dc = Team.objects.create(name='DC', description='DC superheroes')

        # Create users
        tony = User.objects.create(email='tony@stark.com', name='Tony Stark', team=marvel, is_superhero=True)
        steve = User.objects.create(email='steve@rogers.com', name='Steve Rogers', team=marvel, is_superhero=True)
        bruce = User.objects.create(email='bruce@wayne.com', name='Bruce Wayne', team=dc, is_superhero=True)
        clark = User.objects.create(email='clark@kent.com', name='Clark Kent', team=dc, is_superhero=True)

        # Create workouts
        workout1 = Workout.objects.create(name='Super Strength', description='Strength training for heroes', difficulty='Hard')
        workout2 = Workout.objects.create(name='Flight Training', description='Learn to fly', difficulty='Medium')

        # Create activities
        Activity.objects.create(user=tony, type='Iron Suit Training', duration=60, date=date.today())
        Activity.objects.create(user=clark, type='Flight', duration=45, date=date.today())

        # Create leaderboard
        Leaderboard.objects.create(user=tony, score=1000, rank=1)
        Leaderboard.objects.create(user=clark, score=950, rank=2)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))

        # Create teams
        marvel = Team.objects.create(name='Marvel', description='Marvel superheroes')
        dc = Team.objects.create(name='DC', description='DC superheroes')

        # Create users
        tony = User.objects.create(email='tony@stark.com', name='Tony Stark', team=marvel, is_superhero=True)
        steve = User.objects.create(email='steve@rogers.com', name='Steve Rogers', team=marvel, is_superhero=True)
        bruce = User.objects.create(email='bruce@wayne.com', name='Bruce Wayne', team=dc, is_superhero=True)
        clark = User.objects.create(email='clark@kent.com', name='Clark Kent', team=dc, is_superhero=True)

        # Create workouts
        workout1 = Workout.objects.create(name='Super Strength', description='Strength training for heroes', difficulty='Hard')
        workout2 = Workout.objects.create(name='Flight Training', description='Learn to fly', difficulty='Medium')

        # Create activities
        Activity.objects.create(user=tony, type='Iron Suit Training', duration=60, date=date.today())
        Activity.objects.create(user=clark, type='Flight', duration=45, date=date.today())

        # Create leaderboard
        Leaderboard.objects.create(user=tony, score=1000, rank=1)
        Leaderboard.objects.create(user=clark, score=950, rank=2)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
