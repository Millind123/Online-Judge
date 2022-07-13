from django.db import models
from django.utils import timezone as django_tz 



class Problems(models.Model):
    problem_text = models.CharField(max_length=20000)
    problem_name = models.CharField(max_length=20000)
    problem_number  = models.IntegerField(default=0)
    def __str__(self):
        return self.problem_name
    def return_self(self):
        return {self.problem_name,self.problem_text,self.problem_number}


class Inputs(models.Model):
    input_text = models.CharField(max_length=20000)
    input_output = models.CharField(max_length=20000)
    problem_id  = models.IntegerField(default=0)
    inputfile =models.FileField(default='default.txt',upload_to='AllData/inputs')
    outputfile = models.FileField(default='default.txt',upload_to='AllData/outputs')
    def __str__(self):
        return self.input_text
    def return_self(self):
        return {self.input_text,self.input_output,self.problem_number}


class Submission(models.Model):
    submission_ID = models.IntegerField()
    def upload_code_name(self,filename):
        sud = self.submission_ID
        lan = self.submission_language
        return f'AllData/codes/{sud}/{filename}'
    
    
    submission_code = models.FileField(upload_to=upload_code_name)
    submission_verdict = models.CharField(max_length=20000)
    submission_date = models.DateTimeField(default=django_tz.now)
    submission_problemID = models.IntegerField()
    submission_language=models.CharField(max_length=5,default="cpp")
    username = models.CharField(max_length=100)
   

    def __str__(self):
        return self.submission_verdict



