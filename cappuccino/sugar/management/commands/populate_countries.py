from django.core.management.base import BaseCommand
from django_countries import countries
from sugar.models import Country

import logging

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Populates the Country model with data."

    def handle(self, *args, **options):
        count = 0
        try:
            for country in countries:
                Country.objects.create(short_name=country[0],
                                       name=country[1])
                count += 1
                log.info(f"{count} countries have been created so far!")
        except Exception as e:
            log.error(f"Error Creating country {country.name}: {e}")
        log.info("Done!!")
