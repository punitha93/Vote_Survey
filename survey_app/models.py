from django.db import models

class election_survey_details(models.Model):
    PARTY_CONST = {("AAA","AAA"), ("AAB","AAB"), ("AAC","AAC"), ("AAD","AAD")}
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    dob = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    party_name = models.CharField(max_length=20,choices=PARTY_CONST)
    created_on = models.DateTimeField(auto_now=True)

class results_partynames(models.Model):
    party_name = models.CharField(max_length=10)
    vote_count = models.IntegerField()