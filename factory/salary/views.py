from django.shortcuts import render
from django.http import HttpResponse
from .models import labour
from datetime import date,datetime
import math

# Create your views here.


def home(request):
   
    return render (request,'home.html')

def add(request):

   
    num_days=int(request.POST["days"])
    hol_days=int(request.POST["hol_day"])

    drop_str=request.POST["name"]
    x=drop_str.split(',')
    for i in range(0,len(x)):
        x[i]=float(x[i])
        
    


    rate_1= x[0]
    sunday_rate=rate_1*1.5
    emp_id=x[1]
    if emp_id==1:
        emp_name="UMESH SULKAR"
    if emp_id==2:
        emp_name="PRASAD"
    if emp_id==3:
        emp_name="AJAY"
    if emp_id==4:
        emp_name="MALIKARJUN"
    if emp_id==5:
        emp_name="KIRAN"
    if emp_id==6:
        emp_name="ASPAK"
    if emp_id==7:
        emp_name="DASTGIR"
    if emp_id==8:
        emp_name="ARBAZ"
    if emp_id==9:
        emp_name="VINAYAK"
    if emp_id==0:
        emp_name="IRFAN"

    get_month=request.POST["month"]
    get_month=int(get_month)-1
    list_of_months=['January','February','March','April','May','June','July','August','Spetember','October','November','December']
    
    month=str(list_of_months[get_month])

    






    hour_work= int(request.POST["hr"])
    ot_work= int(request.POST["basic_hr"])
    #sun_days=int(request.POST["sun_days"])
    sun_hr=int(request.POST["sun_hr"])
    
    travel= num_days*20
    

    total_hr_routine=hour_work*num_days
    #total_basic_hr=basic_hr_work*num_days
    #extra_time=total_hr_routine-total_basic_hr


    """ calculation """
    actual_wages=total_hr_routine*rate_1
    incentive_amount=(rate_1*8*26)*0.1
    et_wages=ot_work*rate_1
    et_wages=math.ceil(et_wages)
    sun_wages=sun_hr*sunday_rate
    hol_hr=hol_days*8
    hol_wage=hol_hr*rate_1

    """total addition"""
    actual_wages=math.ceil(actual_wages)
    sun_wages=math.ceil(sun_wages)
    incentive_amount=math.ceil(incentive_amount)
    hol_wage=math.ceil(hol_wage)    

    total_wages=actual_wages+et_wages+travel+incentive_amount+sun_wages+hol_wage



    """ceiling all"""
    total_wages=math.ceil(total_wages)


    

#########database connectivity
    # month_info=Month_class(Month=month)
    # month_info.save()


    employee_info_db= labour(emp_name=emp_name,emp_id=emp_id,ot_hr=ot_work,holi_day=hol_days,sunday_hr=sun_hr,Number_days=num_days,basic_wages=actual_wages,extra_wages=et_wages,travel_al=travel,
    sunday_wages=sun_wages,incentive=incentive_amount,holi_wages=hol_wage,final_wages=total_wages)
    
    employee_info_db.save()
    
    


    
    
    return render(request,'results.html',{'name':emp_name,'hol':hol_days,'ot':ot_work,'su':sun_hr,'rate':rate_1,'basic_wages':actual_wages,'Number_days':num_days,'extra':et_wages,
    'travel':travel,'sunday':sun_wages,'incen':incentive_amount,'holiday':hol_wage,'Result':total_wages,'month':month})


#