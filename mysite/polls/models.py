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
    def __str__(self):
        return self.input_text
    def return_self(self):
        return {self.input_text,self.input_output,self.problem_number}


class Submission(models.Model):
    submission_code = models.FileField()
    submission_verdict = models.CharField(max_length=20000)
    submission_date = models.DateTimeField(default=django_tz.now)
    submission_problemID = models.IntegerField()
   

    def __str__(self):
        return self.submission_verdict



