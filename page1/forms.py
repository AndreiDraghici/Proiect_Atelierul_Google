from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.messages import constants as messages
from .models import CustomUser,slm_request,tutorial_model


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model=CustomUser
        fields= UserCreationForm.Meta.fields+ ( 'Name','email','teamname','department','teamleadername','departmentleadername',)

from django.contrib.auth.forms import AuthenticationForm,UsernameField
class CustomAuthenticationForm(AuthenticationForm):
    #nu face nimic
    username= UsernameField()
    


class slm_register_form(forms.ModelForm):
    class Meta:
        model=slm_request

        fields=['responsible','cuet','cuet_IPN','budget','ecu','supplier','system','asil_lvl','pcb_coating','current_pcb_plant','pcb_assembly_plant_transfer','description','description_file','f4_sheet_sent','f4_sheet_sent_file','leading_vehicle_project','leading_vehicle_MA_DATE','application_date','carry_over','lup_number','proof_RNPO','user','status',]

class tutorial_form(forms.ModelForm):
    class Meta:
        model=tutorial_model
        fields=['title','version','description_file',]


'''
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields
'''

