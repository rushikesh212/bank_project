from django.db import models


class Data(models.Model):
    name       = models.CharField(max_length=20, primary_key=True)
    account_no = models.BigIntegerField()
    location   = models.CharField(max_length=30)
    mobile_no  = models.BigIntegerField()
    #image      = models.ImageField(upload_to="images/", null=True)






