from django.core.management import BaseCommand
from you_and_meme_backend_app.models import Meme
import json


class Command(BaseCommand):
    help = 'Load data from a JSON file into the database'

    def add_arguments(self, parser):
        parser.add_argument('json_file', type=str,
                            help='Path to the JSON file')

    def handle(self, *args, **kwargs):
        json_file = kwargs['json_file']

        with open(json_file, 'r') as file:
            data = json.load(file)
            for item in data:
                # Assuming the JSON data directly matches the model fields
                Meme.objects.create(**item)
        self.stdout.write(self.style.SUCCESS('Data imported successfully'))
