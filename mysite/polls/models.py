from django.db import models

# Create your models here.

class Problems(models.Model):
    problem_text = models.CharField(max_length=20000)
    problem_input = models.CharField(max_length=20000)
    problem_output = models.CharField(max_length=20000)
    problem_number  = models.IntegerField(default=0)
    def __str__(self):
        return self.problem_text
    def return_self(self):
        return {self.problem_text,self.problem_input,self.problem_output,self.problem_number}
