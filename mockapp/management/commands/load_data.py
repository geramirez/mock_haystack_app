from django.core.management.base import BaseCommand
from mockapp.scripts import load_data


class Command(BaseCommand):

    help = """ Loads data """

    def handle(self, *args, **options):
        load_data()
