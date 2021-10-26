from django.db import models

# Create your models here.
class testtable(models.Model):
    id=models.AutoField(primary_key=True)
    userName=models.CharField(max_length=500)
    caseId=models.IntegerField()
    caseSection=models.CharField(max_length=500)
    caseDetails=models.CharField(max_length=500)
    caseType=models.CharField(max_length=500)