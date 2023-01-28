from django.db import models
from django.contrib.auth.models import AbstractUser

from django.db.models import Model

class CustomUser(AbstractUser):
    username=models.TextField('IPN',unique= True)
    Name = models.TextField(null= True, blank = True)
    email = models.TextField('E-mail',unique=True,null = True, blank = True)
    teamname = models.TextField('Team Name',null = True, blank = True)
    department = models.TextField(null = True, blank =True)
    teamleadername = models.TextField('Team Leader Name',null = True, blank = True)
    departmentleadername = models.TextField('Department Leader Name',null = True, blank= True)
    is_staff = models.BooleanField(default=False)
    Superuser_status = models.BooleanField(default=False)
    verified = models.BooleanField(default=False)

   

from django import forms
from django.contrib.auth import get_user_model
class slm_request(models.Model):
    user = models.CharField(max_length=100,null=True,blank=True)
    responsible=models.CharField(max_length=100,null=True,blank=True)    
    cuet =models.CharField(max_length=100)
    cuet_IPN=models.CharField(max_length=100)
    budget=models.CharField(max_length=100)
    ecu=models.CharField(max_length=100)
    supplier=models.CharField(max_length=100)
    system=models.CharField(max_length=100)
    asil_lvl=models.CharField(max_length=100)
    pcb_coating=models.CharField(max_length=100)
    current_pcb_plant=models.CharField(max_length=100)
    pcb_assembly_plant_transfer=models.CharField(max_length=100)
    description=models.CharField(max_length=1000)
    description_file=models.FileField(upload_to='Description/',null=True,blank=True)
    f4_sheet_sent=models.CharField(max_length=100)
    f4_sheet_sent_file=models.FileField(upload_to='F4sheets/',null=True,blank=True)
    leading_vehicle_project=models.CharField(max_length=100)
    leading_vehicle_MA_DATE=models.CharField(max_length=100)
    application_date=models.CharField(max_length=100)
    carry_over=models.CharField(max_length=100)
    lup_number=models.CharField(max_length=100)
    proof_RNPO=models.CharField(max_length=100)
    status=models.CharField(max_length=100)
    date = models.DateField(auto_now_add = True)

class slm_request_rejected(models.Model):
    user = models.CharField(max_length=100,null=True,blank=True)
    responsible=models.CharField(max_length=100,null=True,blank=True)    
    cuet =models.CharField(max_length=100)
    cuet_IPN = models.CharField(max_length=100)
    budget=models.CharField(max_length=100)
    ecu=models.CharField(max_length=100)
    supplier=models.CharField(max_length=100)
    system=models.CharField(max_length=100)
    asil_lvl=models.CharField(max_length=100)
    pcb_coating=models.CharField(max_length=100)
    current_pcb_plant=models.CharField(max_length=100)
    pcb_assembly_plant_transfer=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    description_file=models.FileField(upload_to='Description/',null=True,blank=True)
    f4_sheet_sent=models.CharField(max_length=100)
    f4_sheet_sent_file=models.FileField(upload_to='F4sheets/',null=True,blank=True)
    leading_vehicle_project=models.CharField(max_length=100)
    leading_vehicle_MA_DATE=models.CharField(max_length=100)
    application_date=models.CharField(max_length=100)
    carry_over=models.CharField(max_length=100)
    lup_number=models.CharField(max_length=100)
    proof_RNPO=models.CharField(max_length=100)
    status=models.CharField(max_length=100)
    date = models.DateField(auto_now_add = True)
    reason=models.CharField(max_length=1000)

class slm_request_ok(models.Model):
    user = models.CharField(max_length=100,null=True,blank=True)
    responsible=models.CharField(max_length=100,null=True,blank=True)    
    cuet =models.CharField(max_length=100)
    cuet_IPN = models.CharField(max_length=100)
    budget=models.CharField(max_length=100)
    ecu=models.CharField(max_length=100)
    supplier=models.CharField(max_length=100)
    system=models.CharField(max_length=100)
    asil_lvl=models.CharField(max_length=100)
    pcb_coating=models.CharField(max_length=100)
    current_pcb_plant=models.CharField(max_length=100)
    pcb_assembly_plant_transfer=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    description_file=models.FileField(upload_to='Description/',null=True,blank=True)
    f4_sheet_sent=models.CharField(max_length=100)
    f4_sheet_sent_file=models.FileField(upload_to='F4sheets/',null=True,blank=True)
    leading_vehicle_project=models.CharField(max_length=100)
    leading_vehicle_MA_DATE=models.CharField(max_length=100)
    application_date=models.CharField(max_length=100)
    carry_over=models.CharField(max_length=100)
    lup_number=models.CharField(max_length=100)
    proof_RNPO=models.CharField(max_length=100)
    status=models.CharField(max_length=100)
    date = models.DateField(auto_now_add = True)
    date_close = models.DateField(blank=True, null=True)
    slm_number=models.CharField(unique=True,max_length=100)
    comp_status=models.CharField(max_length=100,default='Not Complete')
    comp_change_request=models.CharField(max_length=1000,null=True,blank=True,default='-')
    comp_change_request_status = models.CharField(max_length=1000,null=True,blank=True,default='Not Complete')
    comp_delta= models.CharField(max_length=1000,null=True,blank=True,default='-')
    comp_delta_status=models.CharField(max_length=1000,null=True,blank=True,default='Not Complete')
    comp_updated= models.CharField(max_length=1000,null=True,blank=True,default='-')
    comp_updated_status=models.CharField(max_length=1000,null=True,blank=True,default='Not Complete')
    comp_responsible = models.CharField(max_length =100, null=True, blank=True,default='-')
    comp_time=models.CharField(max_length=100,null=True,blank=True,default='0')
    circuit_status=models.CharField(max_length=100,default='Not Complete')
    circuit_schematics= models.CharField(max_length=1000,null=True,blank=True,default='-')
    circuit_schematics_status=models.CharField(max_length=1000,null=True,blank=True,default='Not Complete')
    circuit_delta_bom= models.CharField(max_length=1000,null=True,blank=True,default='-')
    circuit_delta_bom_status=models.CharField(max_length=1000,null=True,blank=True,default='Not Complete')
    circuit_configuration= models.CharField(max_length=1000,null=True,blank=True,default='-')
    circuit_configuration_status=models.CharField(max_length=1000,null=True,blank=True,default='Not Complete')
    circuit_interface= models.CharField(max_length=1000,null=True,blank=True,default='-')
    circuit_interface_status=models.CharField(max_length=1000,null=True,blank=True,default='Not Complete')
    circuit_hardware_design= models.CharField(max_length=1000,null=True,blank=True,default='-')
    circuit_hardware_design_status=models.CharField(max_length=1000,null=True,blank=True,default='Not Complete')
    circuit_component_derating= models.CharField(max_length=1000,null=True,blank=True,default='-')
    circuit_component_derating_status=models.CharField(max_length=1000,null=True,blank=True,default='Not Complete')
    circuit_abnormal_current= models.CharField(max_length=1000,null=True,blank=True,default='-')
    circuit_abnormal_current_status=models.CharField(max_length=1000,null=True,blank=True,default='Not Complete')
    circuit_responsible = models.CharField(max_length=100,null=True,blank=True,default='-')
    circuit_time=models.CharField(max_length=1000,null=True,blank=True,default='0')
    enviro_status=models.CharField(max_length=100,default='Not Complete')
    enviro_mounting= models.CharField(max_length=1000,null=True,blank=True,default='-')
    enviro_mounting_status=models.CharField(max_length=1000,null=True,blank=True,default='Not Complete')
    enviro_reliability= models.CharField(max_length=1000,null=True,blank=True,default='-')
    enviro_reliability_status=models.CharField(max_length=1000,null=True,blank=True,default='Not Complete')
    enviro_test_reports= models.CharField(max_length=1000,null=True,blank=True,default='-')
    enviro_test_reports_status=models.CharField(max_length=1000,null=True,blank=True,default='Not Complete')
    enviro_responsible = models.CharField(max_length=100, null=True, blank=True,default='-')
    enviro_time=models.CharField(max_length=100, null=True, blank=True,default='0')
    process_status=models.CharField(max_length=100,default='Not Complete')
    process_peses= models.CharField(max_length=1000,null=True,blank=True,default='-')
    process_peses_status=models.CharField(max_length=1000,null=True,blank=True,default='Not Complete')
    process_cutting_edge= models.CharField(max_length=1000,null=True,blank=True,default='-')
    process_cutting_edge_status=models.CharField(max_length=1000,null=True,blank=True,default='Not Complete')
    process_support_activities= models.CharField(max_length=1000,null=True,blank=True,default='-')
    process_support_activities_status=models.CharField(max_length=1000,null=True,blank=True,default='Not Complete')
    process_spp_activities= models.CharField(max_length=1000,null=True,blank=True,default='-')
    process_spp_activities_status=models.CharField(max_length=1000,null=True,blank=True,default='Not Complete')
    process_off_tool = models.CharField(max_length=1000,null=True,blank=True,default='-')
    process_off_tool_status=models.CharField(max_length=1000,null=True,blank=True,default='Not Complete')
    process_qualification_review = models.CharField(max_length=1000, null=True,blank=True,default='-')
    process_qualification_review_status=models.CharField(max_length=1000,null=True,blank=True,default='Not Complete')
    process_responsible = models.CharField(max_length=100,null=True,blank=True,default='-')
    process_time=models.CharField(max_length=100, null=True, blank=True,default='0')
    emc_status=models.CharField(max_length=100,default='Not Complete')
    emc_equipment_test_plan= models.CharField(max_length=1000,null=True,blank=True,default='-')
    emc_equipment_test_plan_status=models.CharField(max_length=1000,null=True,blank=True,default='Not Complete')
    emc_equipment_test_reports= models.CharField(max_length=1000,null=True,blank=True,default='-')
    emc_equipment_test_reports_status=models.CharField(max_length=1000,null=True,blank=True,default='Not Complete')
    emc_vehicle_test= models.CharField(max_length=1000,null=True,blank=True,default='-')
    emc_vehicle_test_status=models.CharField(max_length=1000,null=True,blank=True,default='Not Complete')
    emc_existing_deviations= models.CharField(max_length=1000,null=True,blank=True,default='-')
    emc_existing_deviations_status=models.CharField(max_length=1000,null=True,blank=True,default='Not Complete')
    emc_responsible = models.CharField(max_length=100,null=True,blank=True,default='-')
    emc_time=models.CharField(max_length=100, null=True, blank=True,default='0')
    
    
    
class tutorial_model(models.Model):
    title =models.CharField('Title',max_length=100)
    version=models.CharField('Version',max_length=100)
    date = models.DateField(auto_now_add = True)
    description_file=models.FileField(upload_to='Tutorial/')

    def delete(self, *args, **kwargs):
        self.description_file.delete()
        super().delete(*args, **kwargs)





# Create your models here.