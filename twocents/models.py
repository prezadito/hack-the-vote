from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Bill(models.Model):
    title = models.charfield(max_length=500)
    sponsored_by = models.charfield(max_length=64)
    introduced = models.DateField()
    summary = models.charfield(max_length=1000)
    text = models.charfield(max_length=8000)
    status
    upvotes_downvotes


class User(models.Model):
    party_affiliation
    location
    history


class Vote(models.Model):
    comments
    plus_minus
    User_ID
    Bill_ID
