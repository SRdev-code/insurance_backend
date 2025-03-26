from django.core.management import BaseCommand
from policies.models import PolicyDetails

class Command(BaseCommand):
    def handle(self, *args, **options):

        policies = [
            PolicyDetails(name="Secure Future Term Life", type="Term Life", premium= 5000, coverage= 1000000),
            PolicyDetails(name="Health Shield Plan", type="Health", premium= 3000, coverage= 500000),
            PolicyDetails(name="Car Protect Plan", type="Vehicle", premium= 2000, coverage= 300000),

        ]

        PolicyDetails.objects.bulk_create(policies)
        self.stdout.write(msg="SUCCESS")
        
        # return super().handle(*args, **options)