from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# class Month_class(models.Model):
#     Month=models.CharField(max_length=20)


# def __str__ (self):
#     return self.Month







class labour(models.Model):
    
    #Month_db=models.ForeignKey(Month_class,on_delete=models.CASCADE)
    
    emp_name=models.CharField(max_length=50)
    emp_id=models.IntegerField()
    ot_hr=models.IntegerField()
    holi_day=models.IntegerField()
    sunday_hr=models.IntegerField()
    Number_days=models.IntegerField()
    basic_wages=models.IntegerField()
    extra_wages=models.IntegerField()
    travel_al=models.IntegerField()
    sunday_wages=models.IntegerField()
    incentive=models.IntegerField()
    holi_wages=models.IntegerField()
    final_wages=models.IntegerField()

# def __str__ (self):
#     return self.emp_name + '--' + self.final_wages
    
    #author=models.ForeignKey(User)