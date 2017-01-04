from django.core.management.base import BaseCommand, CommandError
from shortner.models import ShortURL


class Command(BaseCommand):
    help = 'Refreshes all Shortners short_code'

    # def add_arguments(self, parser):
    #     parser.add_argument('poll_id', nargs='+', type=int)

    def handle(self, *args, **options):
        return ShortURL.objects.refresh_shortcode()
