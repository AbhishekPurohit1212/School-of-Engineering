from django.db import models
from django.contrib.auth.models import User

class branch(models.Model):
    branch_id = models.IntegerField(primary_key= True)
    branch_name= models.CharField(max_length= 60)
    def __str__(self):
        return self.branch_name

class subject(models.Model):
    subject_id = models.IntegerField(primary_key=True)
    branch_id = models.ForeignKey(branch, on_delete=models.CASCADE)
    quiz_link = models.CharField(max_length=300)
    subject_name = models.CharField(max_length=100)
    year_id = models.IntegerField()
    def __str__(self):
        return self.subject_name
class resource(models.Model):
    resource_id= models.IntegerField(primary_key=True)
    resource_link= models.CharField(max_length=300)
    subject_id= models.ForeignKey(subject, on_delete=models.CASCADE)
    resource_type= models.CharField(max_length=30)
    resource_name= models.CharField(max_length=200,null=True)
    def __str__(self):
        return str(self.subject_id)+"-"+str(self.resource_type)+"-"+str(self.resource_name)

class review(models.Model):
    subject_id= models.ForeignKey(subject, on_delete=models.CASCADE)
    user_id= models.ForeignKey(User, on_delete=models.CASCADE)
    suggestion= models.CharField(max_length=500)
    def __str__(self):
        return str(self.user_id)+"-"+str(self.subject_id)


