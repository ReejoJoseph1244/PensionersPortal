from django.db import models

# Create your models here.
class NSAP_deatils(models.Model):
    Sl_No = models.IntegerField()
    District = models.CharField(max_length=50)
    Scheme = models.CharField(max_length=15)
    Total_Beneficiary = models.IntegerField()
    Total_Bank = models.IntegerField()
    Total_PO = models.IntegerField()
    Total_MO = models.IntegerField()
    Total_Cash = models.IntegerField()
    Total_Aadhar = models.IntegerField()
    Verified = models.IntegerField()
    Verified_Aadhar_with_bank = models.IntegerField()
    PFMS_Registered = models.IntegerField()
    State = models.CharField(max_length=70)

class CENSUS_Detail(models.Model):
    Country = models.CharField(max_length=50)
    Age = models.IntegerField()
    Total_Males = models.IntegerField()
    Total_Females = models.IntegerField()
    Rural_Males = models.IntegerField()
    Rural_Females = models.IntegerField()
    Urban_Males = models.IntegerField()
    Urban_Females = models.IntegerField()
