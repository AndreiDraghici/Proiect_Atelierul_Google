from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm# , CustomUserChangeForm
from .models import CustomUser
from django import forms


from .forms import slm_register_form
from .models import slm_request
class Slmrequest(admin.ModelAdmin):

    list_display=['id','status','date','user','responsible','cuet','cuet_IPN','budget','ecu','supplier','system','asil_lvl','pcb_coating','current_pcb_plant','pcb_assembly_plant_transfer','description','description_file','f4_sheet_sent','leading_vehicle_project','leading_vehicle_MA_DATE','application_date','carry_over','lup_number','proof_RNPO']

admin.site.register(slm_request,Slmrequest)

from .models import slm_request_rejected
class slm_rejected(admin.ModelAdmin):
    list_display=['id','status','reason','date','user','responsible','cuet','cuet_IPN','budget','ecu','supplier','system','asil_lvl','pcb_coating','current_pcb_plant','pcb_assembly_plant_transfer','description','f4_sheet_sent','leading_vehicle_project','leading_vehicle_MA_DATE','application_date','carry_over','lup_number','proof_RNPO']
admin.site.register(slm_request_rejected,slm_rejected)

from .models import slm_request_ok
class slm_ok(admin.ModelAdmin):
    list_display=['id','status','slm_number','date','date_close','user','responsible','cuet','cuet_IPN','budget','ecu','supplier','system','asil_lvl','pcb_coating','current_pcb_plant','pcb_assembly_plant_transfer','description','description_file','f4_sheet_sent','leading_vehicle_project','leading_vehicle_MA_DATE','application_date','carry_over','lup_number','proof_RNPO','comp_change_request']
admin.site.register(slm_request_ok,slm_ok)

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
 #   form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username','Name','email','teamname','department','teamleadername','departmentleadername','is_staff','Superuser_status','verified']

admin.site.register(CustomUser, CustomUserAdmin)



# Register your models here.

