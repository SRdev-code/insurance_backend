from django.db import models

# Create your models here.
# [
#   {
#     "id": 1,
#     "name": "Secure Future Term Life",
#     "type": "Term Life",
#     "premium": 5000,
#     "coverage": 1000000
#   },
#   {
#     "id": 2,
#     "name": "Health Shield Plan",
#     "type": "Health",
#     "premium": 3000,
#     "coverage": 500000
#   },
#   {
#     "id": 3,
#     "name": "Car Protect Plan",
#     "type": "Vehicle",
#     "premium": 2000,
#     "coverage":   
#   }
# ]


class PolicyDetails(models.Model):
    POLICY_TYPES = [
        ('Term Life', 'Term Life'),
        ('Health', 'Health'),
        ('Vechile', 'Vechile'),
    ]

    name = models.CharField(max_length=255)
    type = models.CharField(max_length=50, choices=POLICY_TYPES)
    premium = models.IntegerField()
    coverage = models.IntegerField()


    def __str__(self):
        return self.name
