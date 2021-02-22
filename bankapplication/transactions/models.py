from django.db import models

# Create your models here.
class Transferdetails(models.Model):
    account_number = models.CharField(max_length=100)
    amount = models.IntegerField()
    mpin = models.IntegerField()


    def __str__(self):
        return self.mpin+ self.account_number