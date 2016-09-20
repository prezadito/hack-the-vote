from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=64)

    DEMOCRAT = 'DEM'
    REPUBLICAN = 'REP'
    THIRD_PARTY = 'THIRD'
    INDEPENDENT = 'IND'
    PARTY_AFFILIATION_CHOICES = (
        (DEMOCRAT, 'Democrat'),
        (REPUBLICAN, 'Republican'),
        (THIRD_PARTY, 'Third Party'),
        (INDEPENDENT, 'Independent')
    )

    party_affiliation = models.CharField(
        max_length = 2,
        choices = PARTY_AFFILIATION_CHOICES,
        default = INDEPENDENT
    )

    def __str__(self):
        return self.name

    # location


class Bill(models.Model):
    name = models.CharField(max_length=64)
    author = models.ForeignKey('auth.user')
    proposed_date = models.DateTimeField(blank=True, null=True)
    summary = models.CharField(max_length=148)
    text = models.TextField()
    userUpVotes = models.ManyToManyField(User, blank=True, related_name='billUpVotes')
    userDownVotes = models.ManyToManyField(User, blank=True, related_name='billDownVotes')

    def propose(self):
        self.proposed_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name

# class Vote(models.Model):
#     comments
#     plus_minus
#     User_ID
#     Bill_ID
