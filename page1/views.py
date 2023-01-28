from django.views.generic import TemplateView,DetailView,CreateView,ListView
from .models import tutorial_model
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.views import LoginView
from .forms import CustomAuthenticationForm,slm_register_form,tutorial_form
from django.shortcuts import redirect,render,get_object_or_404
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy
from .models import slm_request_rejected,slm_request_ok, slm_request, CustomUser
from datetime import datetime
import xlwt
class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm

class login(TemplateView):
    template_name='registration/login.html'


def slmregister(request):
    form = None
    username = None
    post = request.POST.copy()
    username = request.user.username
    post['user'] = username
    post['status'] = 'To be reviewed'
    print(post['user'])
    request.POST = post
   # form=slm_register_form(post)
    form=slm_register_form(request.POST,request.FILES)

    if form.is_valid():
        form.save()
        form=slm_register_form()# pentru a scoate textul deja inserat anterior dupa submit
        return HttpResponseRedirect('/history/')
    context = {
        'form' : form
        }    
   # return HttpResponseRedirect('/history/')
    return render(request,'slmregister.html',context)





def superuser(request): #modificata din clasa in functie pentru a afisa obiectele in super user
   # template_name='superuser.html'
   obj=slm_request.objects.all()
   context ={
              'objects' : obj
              }
   return render(request, "superuser.html",context)

def history(request):
    slm_pending = slm_request.objects.all()
    slm_nok = slm_request_rejected.objects.all()
    slm_ok = slm_request_ok.objects.all()
    total = list(slm_pending)+list(slm_nok) + list(slm_ok)
    total = sorted(total, key=lambda x: x.date, reverse=True)
    context ={
            'objects':total
            }
    return render(request,"history.html",context)

def history_all(request):
    slm_pending = slm_request.objects.all()
    slm_nok = slm_request_rejected.objects.all()
    slm_ok = slm_request_ok.objects.all()
    total = list(slm_pending)+list(slm_nok) + list(slm_ok)
    total = sorted(total, key=lambda x: x.date, reverse=True)
    context ={
            'objects':total
            }
    return render(request,"history_all.html",context)

def history_slm_all(request):
        number = request.POST.get("slm_number","")
        print(number)
        slm = slm_request_ok.objects.get(slm_number = number)
        context={ 'object':slm}
        return render(request,"history_slm_all.html",context)

def history_slm(request):
        number = request.POST.get("slm_number","")
        print(number)
        slm = slm_request_ok.objects.get(slm_number = number)
        context={ 'object':slm}        
        return render(request,"history_slm.html",context)

def suivi(request):
        slm = slm_request_ok.objects.all()
        context ={
                'objects':slm
                }
        return render(request, "suivi.html", context)

class superusermenu(TemplateView):
    template_name='superusermenu.html'

#pagina pentru afisare detalii slm_request
# trebuie schimbata clasa din care face parte in CreateView pentru a folosi form
from django.http import HttpResponse
class slm_request_detail(DetailView):
    template_name="details.html"

    def get_object(self):
        id_=self.kwargs.get("id")
        return get_object_or_404(slm_request, id=id_)

    from .models import slm_request 
    from django.db import models
    def notok(request):
        id_ = request.POST.get("nok","")
        obj = slm_request.objects.get(id=id_)
        obj_reason=request.POST.get("Reason","")
        slm_rejected = slm_request_rejected.objects.create(cuet=obj.cuet,cuet_IPN=obj.cuet_IPN,user=obj.user,
                responsible=obj.responsible,budget=obj.budget,ecu=obj.ecu,supplier=obj.supplier,
                system=obj.system, asil_lvl=obj.asil_lvl, pcb_coating= obj.pcb_coating,
                current_pcb_plant = obj.current_pcb_plant,pcb_assembly_plant_transfer= obj.pcb_assembly_plant_transfer,
                description = obj.description,description_file = obj.description_file,
                 f4_sheet_sent = obj.f4_sheet_sent,f4_sheet_send_file = obj.f4_sheet_sent_file,
                leading_vehicle_project =obj.leading_vehicle_project,
                leading_vehicle_MA_DATE = obj.leading_vehicle_MA_DATE, 
                application_date = obj.application_date,
                carry_over = obj.carry_over, lup_number = obj.lup_number,
                proof_RNPO= obj.proof_RNPO, status = "Not Eligible",reason=obj_reason )
        slm_rejected.save()
        obj.delete()
       # return HttpResponse('homepage')
        return HttpResponseRedirect('/homepage/')
     
    def ok(request):
        id_=request.POST.get("ok","")
        slm_old = slm_request.objects.get(id=id_)
        obj = request.POST
        obj_nr=request.POST.get("nr","")

        slm_ok = slm_request_ok.objects.create(cuet=obj["cuet"],cuet_IPN=obj["cuet_ipn"],user=obj["user"],
                responsible=obj["responsible"],budget=obj["budget"],ecu=obj["ecu"],supplier=obj["supplier"],
                system=obj["system"], asil_lvl=obj["asil_lvl"], pcb_coating= obj["pcb_coating"],
                current_pcb_plant = obj["current_pcb_plant"],pcb_assembly_plant_transfer= obj["pcb_assembly_plant_transfer"],
                description = obj["description"],description_file = slm_old.description_file, f4_sheet_sent = obj["f4_sheet_sent"],
                f4_sheet_sent_file = slm_old.f4_sheet_sent_file, leading_vehicle_project =obj["leading_vehicle_project"],
                leading_vehicle_MA_DATE = obj["leading_vehicle_MA_DATE"], 
                application_date = obj["application_date"],
                carry_over = obj["carry_over"], lup_number = obj["lup_number"],
                proof_RNPO= obj["proof_RNPO"], status = "Ongoing",slm_number=obj_nr )
        slm_ok.save()
        slm_old.delete()
        return HttpResponseRedirect('/homepage/')
        
def slm_done(request): 
        import datetime
        from datetime import datetime
        slm= slm_request_ok.objects.all()
        context ={
            'slm':slm
                }
        if request.method=="POST":
                nr = request.POST.get("nr","")
                print(nr)
                for i in slm:
                        if i.slm_number == nr:
                                i.status = "Done"
                                i.date_close = datetime.now()
                                i.save()
        return render(request,'slm_done.html',context)
        
        
def changeipn(request):
    if request.method == "POST":
        obj=request.POST
        oldipn=(obj['oldipn'])
        newipn=(obj['newipn'])
        print(newipn) 
        slm_list = slm_request.objects.all()
        for i in slm_list:
            print(i.user)
            if i.user == oldipn:
                i.user = newipn
                i.save()
        slm_list_nok = slm_request_rejected.objects.all()
        for i in slm_list_nok:
            if i.user == oldipn:
                i.user=newipn
                i.save()

        return HttpResponseRedirect('/homepage/')
    return render(request,"changeipn.html")
    
def changecuet(request):
    if request.method == "POST":
        obj=request.POST
        oldipn=(obj['oldipn'])
        newipn=(obj['newipn'])
        cuet=(obj['name'])
        print(newipn) 
        slm_list_ok = slm_request_ok.objects.all()
        for i in slm_list_ok:
            if i.cuet_IPN == oldipn:
                i.cuet_IPN = newipn
                i.cuet = cuet
                i.save()
        slm_list = slm_request.objects.all()
        for i in slm_list:
            if i.cuet_IPN == oldipn:
                i.cuet_IPN = newipn
                i.cuet = cuet
                i.save()
        slm_list_nok = slm_request_rejected.objects.all()
        for i in slm_list_nok:
            if i.cuet_IPN == oldipn:
                i.cuet_IPN=newipn
                i.cuet = cuet
                i.save()

        return HttpResponseRedirect('/homepage/')
    return render(request,"changecuet.html")
    
def make_specialist(request):
    if request.method== "POST":
        obj=request.POST
        ipn = (obj['ipn_user'])
        print(ipn)
        user_list = CustomUser.objects.all()
        for i in user_list:
            if i.username == ipn:
                i.is_staff = True
                i.save()
        return HttpResponseRedirect('/homepage/')
    return render(request,"make_specialist.html")
 
def remove_specialist(request):
    if request.method== "POST":
        obj=request.POST
        ipn = (obj['ipn_user'])
        print(ipn)
        user_list = CustomUser.objects.all()
        for i in user_list:
            if i.username == ipn:
                i.is_staff = False
                i.save()
        return HttpResponseRedirect('/homepage/')
    return render(request,"remove_specialist.html")
    
def make_superuser(request):
    if request.method== "POST":
        obj=request.POST
        ipn = (obj['ipn_user'])
        print(ipn)
        user_list = CustomUser.objects.all()
        for i in user_list:
            print(i)
            if i.username == ipn:
                i.Superuser_status = True
                i.is_staff = True
                i.verified = True
                i.save()
        return HttpResponseRedirect('/homepage/')
    return render(request,"make_superuser.html")
    
def remove_superuser(request):
    if request.method== "POST":
        obj=request.POST
        ipn = (obj['ipn_user'])
        print(ipn)
        user_list = CustomUser.objects.all()
        for i in user_list:
            if i.username == ipn:
                i.Superuser_status = False
                i.save()
        return HttpResponseRedirect('/homepage/')
    return render(request,"remove_superuser.html")    

    
def specialist_menu(request):
    obj=slm_request_ok.objects.all()
    obj = obj.order_by("-slm_number")
    context={
        'objects':obj
        }
    return render(request,"specialist_menu.html",context)

def users_and_staff(request):
    print("users and staff")
    users=[]
    specialists=[]
    superusers=[]
    user_list = CustomUser.objects.all()
    for i in user_list:
        if i.Superuser_status == True:
            superusers.append(i)
        elif i.is_staff == True:
            specialists.append(i)
        else:
            users.append(i)
    context ={
            'users':users,
            'specialists':specialists,
            'superusers':superusers
                }
    print(superusers)
    print(specialists)
    print(users)
    return render(request,'users_and_staff.html',context)

    

slm_nr = ""
class slm_number_detail(DetailView):
    template_name="slm_number_detail.html"
    def get_object(self):
        slm_number_ = self.kwargs.get("slm_number")
        return get_object_or_404(slm_request_ok, slm_number=slm_number_)
    
    def components(request):
        nr_ = request.POST.get("components","")
        global slm_nr
        slm_nr=nr_
        obj = slm_request_ok.objects.get(slm_number = nr_)
        return HttpResponseRedirect('/components_review')
    def circuit(request):
        nr_ = request.POST.get("circuit","")
        print("CIRCUIT")
        global slm_nr
        slm_nr=nr_
        obj = slm_request_ok.objects.get(slm_number = nr_)
        return HttpResponseRedirect('/circuit_review')
        
    def enviro(request):
        nr_ = request.POST.get("enviro","")
        global slm_nr
        slm_nr=nr_
        obj = slm_request_ok.objects.get(slm_number = nr_)
        return HttpResponseRedirect('/enviro_review')
        
    def process(request):
        nr_ = request.POST.get("process","")
        global slm_nr
        slm_nr=nr_
        obj = slm_request_ok.objects.get(slm_number = nr_)
        return HttpResponseRedirect('/process_review')
        
    def emc(request):
        nr_ = request.POST.get("emc","")
        global slm_nr
        slm_nr=nr_
        obj = slm_request_ok.objects.get(slm_number = nr_)
        return HttpResponseRedirect('/emc_review')

def components_review(request):
        global slm_nr
        slm= slm_request_ok.objects.get(slm_number = slm_nr)
        print(slm_nr)
        context ={
                'slm':slm
            }
        if request.method=="POST":
                obj=request.POST
                comp_change = obj['comp_change']
                comp_change_status = obj['comp_change_status']
                comp_delta = obj['comp_delta']
                comp_delta_status = obj['comp_delta_status']
                comp_updated = obj['comp_updated']
                comp_updated_status=obj['comp_updated_status']
                comp_status = obj['status']
                comp_responsible = obj['comp_responsible']
                comp_time = obj['comp_time']
                print(slm_nr)
                slm = slm_request_ok.objects.get(slm_number = slm_nr)
                slm.comp_change_request = comp_change
                slm.comp_change_request_status = comp_change_status
                slm.comp_delta = comp_delta
                slm.comp_delta_status = comp_delta_status
                slm.comp_updated = comp_updated
                slm.comp_updated_status = comp_updated_status
                slm.comp_status = comp_status
                slm.comp_responsible = comp_responsible
                slm.comp_time = comp_time
                slm.save()
                return HttpResponseRedirect('/specialist_menu/')
        return render(request,"components_review.html",context)
def circuit_review(request):
    global slm_nr
    slm= slm_request_ok.objects.get(slm_number = slm_nr)
    context ={
        'slm':slm
        }
    if request.method=="POST":
        obj=request.POST
        circuit_schematics = obj['circuit_schematics']
        circuit_schematics_status = obj['circuit_schematics_status']
        circuit_delta_bom = obj['circuit_delta_bom']
        circuit_delta_bom_status = obj['circuit_delta_bom_status']
        circuit_configuration = obj['circuit_configuration']
        circuit_configuration_status = obj['circuit_configuration_status']
        circuit_interface= obj['circuit_interface']
        circuit_interface_status = obj['circuit_interface_status']
        circuit_hardware_design= obj['circuit_hardware_design']
        circuit_hardware_design_status = obj['circuit_hardware_design_status']
        circuit_component_derating= obj['circuit_component_derating']
        circuit_component_derating_status = obj['circuit_component_derating_status']
        circuit_abnormal_current= obj['circuit_abnormal_current']
        circuit_abnormal_current_status = obj['circuit_abnormal_current_status']
        circuit_responsible= obj['circuit_responsible']
        circuit_status = obj['status']
        circuit_time = obj['circuit_time']
        
        print(circuit_responsible)
        slm = slm_request_ok.objects.get(slm_number = slm_nr)
        slm.circuit_schematics = circuit_schematics
        slm.circuit_schematics_status = circuit_schematics_status
        slm.circuit_delta_bom = circuit_delta_bom
        slm.circuit_delta_bom_status = circuit_delta_bom_status
        slm.circuit_configuration = circuit_configuration
        slm.circuit_configuration_status = circuit_configuration_status
        slm.circuit_interface =circuit_interface 
        slm.circuit_interface_status = circuit_interface_status
        slm.circuit_hardware_design=circuit_hardware_design
        slm.circuit_hardware_design_status = circuit_hardware_design_status
        slm.circuit_component_derating=circuit_component_derating
        slm.circuit_component_derating_status = circuit_component_derating_status
        slm.circuit_abnormal_current=circuit_abnormal_current
        slm.circuit_abnormal_current_status = circuit_abnormal_current_status
        slm.circuit_responsible=circuit_responsible
        slm.circuit_status=circuit_status
        slm.circuit_time = circuit_time
        slm.save()
        return HttpResponseRedirect('/specialist_menu/')
    return render(request,"circuit_review.html",context)
def enviro_review(request):
    global slm_nr
    slm= slm_request_ok.objects.get(slm_number = slm_nr)
    context ={
        'slm':slm
        }
    if request.method=="POST":
        obj=request.POST
        enviro_mounting = obj['enviro_mounting']
        enviro_mounting_status = obj['enviro_mounting_status']
        enviro_reliability = obj['enviro_reliability']
        enviro_reliability_status = obj['enviro_reliability_status']
        enviro_test_reports = obj['enviro_test_reports']
        enviro_test_reports_status = obj ['enviro_test_reports_status']
        enviro_responsible = obj['enviro_responsible']
        enviro_status = obj['status']
        enviro_time = obj['enviro_time']
        slm = slm_request_ok.objects.get(slm_number = slm_nr)
        slm.enviro_mounting= enviro_mounting
        slm.enviro_mounting_status = enviro_mounting_status
        slm.enviro_reliability= enviro_reliability
        slm.enviro_reliability_status = enviro_reliability_status
        slm.enviro_test_reports = enviro_test_reports
        slm.enviro_test_reports_status = enviro_test_reports_status
        slm.enviro_responsible = enviro_responsible
        slm.enviro_status = enviro_status
        slm.enviro_time = enviro_time
        slm.save()
        return HttpResponseRedirect('/specialist_menu/')
    return render(request,"enviro_review.html",context)
def process_review(request):
    global slm_nr
    slm= slm_request_ok.objects.get(slm_number = slm_nr)
    context ={
        'slm':slm
        }
    if request.method=="POST":
        obj=request.POST
        process_peses = obj['process_peses']
        process_peses_status = obj['process_peses_status']
        process_cutting_edge =obj['process_cutting_edge']
        process_cutting_edge_status = obj['process_cutting_edge_status']
        process_support_activities=obj['process_support_activities']
        process_support_activities_status = obj['process_support_activities_status']
        process_spp_activities=obj['process_spp_activities']
        process_spp_activities_status=obj['process_spp_activities_status']
        process_off_tool=obj['process_off_tool']
        process_off_tool_status = obj['process_off_tool_status']
        process_qualification_review=obj['process_qualification_review']
        process_qualification_review_status = obj['process_qualification_review_status']
        process_responsible=obj['process_responsible']
        process_status=obj['status']
        process_time = obj['process_time']
        slm = slm_request_ok.objects.get(slm_number = slm_nr)
        slm.process_peses = process_peses
        slm.process_peses_status = process_peses_status
        slm.process_cutting_edge = process_cutting_edge
        slm.process_cutting_edge_status = process_cutting_edge_status
        slm.process_support_activities = process_support_activities
        slm.process_support_activities_status = process_support_activities_status
        slm.process_spp_activities = process_spp_activities
        slm.process_spp_activities_status = process_spp_activities_status
        slm.process_off_tool = process_off_tool
        slm.process_off_tool_status = process_off_tool_status
        slm.process_qualification_review = process_qualification_review
        slm.process_qualification_review_status = process_qualification_review_status
        slm.process_responsible = process_responsible
        slm.process_status = process_status
        slm.process_time = process_time
        slm.save()
        return HttpResponseRedirect('/specialist_menu/')
    return render(request,"process_review.html",context)
def emc_review(request):
    global slm_nr
    slm= slm_request_ok.objects.get(slm_number = slm_nr)
    context ={
        'slm':slm
        }
    if request.method=="POST":
        obj=request.POST
        emc_status = obj['status']
        emc_responsible = obj['emc_responsible']
        emc_equipment_test_plan = obj['emc_equipment_test_plan']
        emc_equipment_test_plan_status = obj['emc_equipment_test_plan_status']
        emc_equipment_test_reports = obj['emc_equipment_test_reports']
        emc_equipment_test_reports_status = obj['emc_equipment_test_reports_status']
        emc_vehicle_test = obj['emc_vehicle_test']
        emc_vehicle_test_status = obj['emc_vehicle_test_status']
        emc_existing_deviations = obj['emc_existing_deviations']
        emc_existing_deviations_status = obj['emc_existing_deviations_status']
        emc_time = obj['emc_time']
        slm = slm_request_ok.objects.get(slm_number = slm_nr)
        slm.emc_status=emc_status
        slm.emc_responsible = emc_responsible
        slm.emc_equipment_test_plan = emc_equipment_test_plan
        slm.emc_equipment_test_plan_status = emc_equipment_test_plan_status
        slm.emc_equipment_test_reports = emc_equipment_test_reports
        slm.emc_equipment_test_reports_status = emc_equipment_test_reports_status
        slm.emc_vehicle_test = emc_vehicle_test
        slm.emc_vehicle_test_status = emc_vehicle_test_status
        slm.emc_existing_deviations = emc_existing_deviations
        slm.emc_existing_deviations_status = emc_existing_deviations_status
        slm.emc_time = emc_time
        slm.save()
        return HttpResponseRedirect('/specialist_menu/')
    return render(request,"emc_review.html",context)



def export_karte_pdf(request):
    from django.core.files.storage import FileSystemStorage
    from django.http import HttpResponse
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import cm, inch
    from reportlab.lib.pagesizes import A4
    from reportlab.lib import colors
    
    obj=request.POST
    slm_nr = obj['slm_nr']
    slm= slm_request_ok.objects.get(slm_number = slm_nr)
    temp = vars(slm)
    columns = ['User','PDE','Cuet','Cuet IPN','Budget','ECU','Supplier','System','Asil lvl','PCB Coating','Current PCB Plant',
    'PCB Assembly Plant Transfer','Description','F4 Sheet','Leading Vehicle Project','Leading Vehicle MA Date',
    'Application Date','Carry Over','Lup Nr','Buyer','Status','Open Date','Close Date','SLM No.',
    'Comp Status','Comp Change Request','Comp Change Request Status','Delta AECQ','Delta AECQ Status','Comp1 Update','Comp1 Update Status','Components Responsible',
    'Load(days)','Circuit Status','Schematics','Schematics Status','Delta BOM','Delta BOM Status','Circuit Configuration','Circuit Configuration Status',
    'Interface Specification','Interface Specification Status','Hardware Design','Hardware Design Status','Component Derating','Component Derating Status',
    'Abnormal Current','Abnormal Current Status','Circuit Responsible','Load(days)','Enviro Status','Mounting Part','Mounting Part Status','Reliability Test',
    'Reliability Test Status','Test Reports Review','Test Reports Review Status','EMC Responsible','Load(days)','Process Status','Peses','Peses Status',
    'Cutting Edge Process','Cutting Edge Process Status','Support Activities','Support Activities Status','SPP Activities','SPP Activities Status',
    'Off-Tool Board Quality','Off-Tool Board Quality Status','Process Qualification','Process Qualification Status','Process Responsible','Load(days)',
    'EMC Status','Equipment Test Plan','Equipment Test Plan Status','Equipment Test Reports','Equipment Test Reports Status','Vehicle Test','Vehicle Test Status',
    'Existing Deviations','Existing Deviations Status','EMC Responsible','Load(days)']

    doc = SimpleDocTemplate("/tmp/Karte.pdf",pagesize=A4,
                        rightMargin=1*cm,leftMargin=1*cm,
                        topMargin=0.5*cm,bottomMargin=2*cm)
    styles = getSampleStyleSheet()
    Story = [Spacer(1,2 * inch)]
    style = styles["Normal"]
    styleH = styles['Heading1']
    styleH.fontSize=25
    styleH.aligment='TA_CENTER'
    styleH.leading=20
    title='Karte_'
    title=title+ slm_nr
    doc.title=title
    elements = []
    k=0
    import datetime
    #titluStyle = ParagraphStyle('test',aligment='CENTER', fontsize=50, fontName='Times-Roman')
    titlu = Paragraph(title,styleH)
    Story.append(titlu)
    for item in temp:
            if k==0 or k==1:
                    print("")
            elif item=="description_file" or item=="f4_sheet_sent_file":
                    k=k-1
            else:
                    #print(item, " : " , temp[item])
                    #print("\n")
                    #print(k, "  ", columns[k-2],"  ",temp[item])
                    col1=columns[k-2]
                    if (isinstance(temp[item],datetime.date)) is True:
                            t=temp[item].strftime("%d/%m/%Y")

                    else:
                            t=temp[item]
                    if type(t) == 'NoneType':
                        t=" "
                    if type(col1) == 'NoneType':
                        col1=" "
                    col1=str(col1)+"  " +str(t)
                    p = Paragraph(col1,style)
                    Story.append(p)
                    #p = Paragraph(t,style)
                    #Story.append(p)
                    
                    Story.append(Spacer(1,1*cm))
            k=k+1
    doc.build(Story)



    # write the document to disk
    #doc.build(elements)
    #doc.build([Paragraph(getSampleStyleSheet()['Normal']),])
    #doc.build(Story)
    
    fs = FileSystemStorage("/tmp")
    title=title+".pdf"
    print(title)
    with fs.open("Karte.pdf") as pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="{}"'.format(title)
        return response

    return response


def export_suivi_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Suivi.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Suivi')
    ws.width=256*40

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['SLM No.','Open Date','Close Date','Status','User','PDE','Cuet','Cuet IPN','Budget','ECU','Supplier','System','Asil lvl','PCB Coating','Current PCB Plant',
    'PCB Assembly Plant Transfer','Description','F4 Sheet','Leading Vehicle Project','Leading Vehicle MA Date','Application Date','Carry Over','Lup Nr','Buyer',
    'Comp Status','Comp Change Request','Comp Change Request Status','Delta AECQ','Delta AECQ Status','Comp1 Update','Comp1 Update Status','Components Responsible',
    'Load(days)','Circuit Status','Schematics','Schematics Status','Delta BOM','Delta BOM Status','Circuit Configuration','Circuit Configuration Status',
    'Interface Specification','Interface Specification Status','Hardware Design','Hardware Design Status','Component Derating','Component Derating Status',
    'Abnormal Current','Abnormal Current Status','Circuit Responsible','Load(days)','Enviro Status','Mounting Part','Mounting Part Status','Reliability Test',
    'Reliability Test Status','Test Reports Review','Test Reports Review Status','EMC Responsible','Load(days)','Process Status','Peses','Peses Status',
    'Cutting Edge Process','Cutting Edge Process Status','Support Activities','Support Activities Status','SPP Activities','SPP Activities Status',
    'Off-Tool Board Quality','Off-Tool Board Quality Status','Process Qualification','Process Qualification Status','Process Responsible','Load(days)',
    'EMC Status','Equipment Test Plan','Equipment Test Plan Status','Equipment Test Reports','Equipment Test Reports Status','Vehicle Test','Vehicle Test Status',
    'Existing Deviations','Existing Deviations Status','EMC Responsible','Load(days)']

    for col_num in range(len(columns)):
        ws.col(col_num).width = 256*25
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = slm_request_ok.objects.all().values_list('slm_number','date','date_close','status','user','responsible','cuet','cuet_IPN','budget','ecu','supplier','system','asil_lvl',
    'pcb_coating','current_pcb_plant','pcb_assembly_plant_transfer','description','f4_sheet_sent','leading_vehicle_project','leading_vehicle_MA_DATE','application_date',
    'carry_over','lup_number','proof_RNPO','comp_status','comp_change_request','comp_change_request_status','comp_delta','comp_delta_status','comp_updated','comp_updated_status',
    'comp_responsible','comp_time','circuit_status','circuit_schematics','circuit_schematics_status','circuit_delta_bom','circuit_delta_bom_status','circuit_configuration',
    'circuit_configuration_status','circuit_interface','circuit_interface_status','circuit_hardware_design','circuit_hardware_design_status','circuit_component_derating',
    'circuit_component_derating_status','circuit_abnormal_current','circuit_abnormal_current_status','circuit_responsible','circuit_time','enviro_status','enviro_mounting',
    'enviro_mounting_status','enviro_reliability','enviro_reliability_status','enviro_test_reports','enviro_test_reports_status','enviro_responsible','enviro_time',
    'process_status','process_peses','process_peses_status','process_cutting_edge','process_cutting_edge_status','process_support_activities','process_support_activities_status',
    'process_spp_activities','process_spp_activities_status','process_off_tool','process_off_tool_status','process_qualification_review','process_qualification_review_status',
    'process_responsible','process_time','emc_status','emc_equipment_test_plan','emc_equipment_test_plan_status','emc_equipment_test_reports','emc_equipment_test_reports_status',
    'emc_vehicle_test','emc_vehicle_test_status','emc_existing_deviations','emc_existing_deviations_status','emc_responsible','emc_time')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    import itertools
    try:
            for i in itertools.count():
                    wb.col(i).width=width
    except:
            pass
    wb.save(response)
    return response    
    
    
    
import datetime
def statistics(request):
        list_months=['January','February','March','April','May','June','July','August','September','October','November','December']
        list_nr=[0,0,0,0,0,0,0,0,0,0,0,0]
        team_impact=[0,0,0,0,0,0] #comp,circuit,enviro,process,emc,total
        team_impact_name=['Components','Circuit','Enviro','Process','EMC','Total Impacted']
        ecu = []
        supplier = []
        car = []
        if request.method=="POST":
                year=request.POST.get("year","")
                print(year)
                all_slm = slm_request_ok.objects.all()
                total=0
                for i in all_slm:
                        if i.slm_number[4:8] == year:
                                # team impact
                                k=0
                                if i.comp_status != "Not Complete" and i.comp_status!= "NO IMPACT":
                                        team_impact[0]+=1
                                        k=1
                                if i.circuit_status != "Not Complete" and i.comp_status!= "NO IMPACT":
                                        team_impact[1]+=1
                                        k=1
                                if i.enviro_status != "Not Complete" and i.comp_status!= "NO IMPACT":
                                        team_impact[2]+=1
                                        k=1
                                if i.process_status != "Not Complete" and i.comp_status!= "NO IMPACT":
                                        team_impact[3]+=1
                                        k=1
                                if i.emc_status != "Not Complete" and i.comp_status!= "NO IMPACT":
                                        team_impact[4]+=1
                                        k=1
                                if k == 1:        
                                        team_impact[5]+=1
                                #car stats
                                ecu.append(i.ecu)
                                supplier.append(i.supplier)
                                car.append(i.leading_vehicle_project)
                                
                                #slm / month 
                                total+=1
                                t=i.date.strftime("%d/%m/%Y")
                                data = t[3:5]
                                data.strip("0")
                                list_nr[int(data)]+=1
                ecu.sort()
                supplier.sort()
                car.sort()
                k=0
                ecu_nr=[]
                ecu_name=[]
                supplier_nr=[]
                supplier_name=[]
                car_nr=[]
                car_name=[]
                nr=0
                for i in ecu:
                        
                        if k != 0:
                                if i == ecu[k-1]:
                                        nr+=1
                                else:
                                        ecu_name.append(i)
                                        ecu_nr.append(nr)
                                        nr=1
                                        
                        else:
                                ecu_name.append(i)
                                nr=1
                                
                        k += 1
                ecu_nr.append(nr)
                k=0
                n=0
                for i in supplier:
                        
                        if k != 0:
                                if i == supplier[k-1]:
                                        nr+=1
                                else:
                                        supplier_name.append(i)
                                        supplier_nr.append(nr)
                                        nr=1
                                        
                        else:
                                supplier_name.append(i)
                                nr=1
                                
                        k += 1
                supplier_nr.append(nr)                
                k=0
                n=0
                for i in car:
                        
                        if k != 0:
                                if i == car[k-1]:
                                        nr+=1
                                else:
                                        car_name.append(i)
                                        car_nr.append(nr)
                                        nr=1
                                        
                        else:
                                car_name.append(i)
                                nr=1
                                
                        k += 1
                car_nr.append(nr)                  
                
                
                
                
                
                
                print("AAAAAAAAAAAAAAAAAAAAAAAA")
                for i in range(len(ecu_name)):
                        print(ecu_name[i]," ",ecu_nr[i])
                print("AAAAAAAAAAAAAAAAAAAAAAAA")
                for i in range(len(supplier_name)):
                        print(supplier_name[i]," ",supplier_nr[i])
                for i in range(len(car_name)):
                        print(car_name[i]," ",car_nr[i])
                for i in range(12):
                        print(list_months[int(i)],"  ",list_nr[int(i)])
                print(team_impact[5])
                response = HttpResponse(content_type='application/ms-excel')
                response['Content-Disposition'] = 'attachment; filename="Statistics1.xls"'
                wb = xlwt.Workbook(encoding='utf-8')
                ws = wb.add_sheet('1')
                ws.width=256*80
                # Sheet header, first row
                row_num = 0
                font_style = xlwt.XFStyle()
                font_style.font.bold = True
                '''
                for col_num in range(len(list_months)):
                        ws.col(col_num).width = 256*10
                        ws.write(row_num, col_num, list_months[col_num], font_style) 
                '''
                font_style = xlwt.XFStyle()      
                '''        
                for row in range(1):
                        row_num += 1
                        for col_num in range(12):
                            ws.write(row_num, col_num, list_nr[col_num], font_style)
                '''
                ws.write(0,0,"TOTAL:",font_style)
                ws.write(0,1,total,font_style)
                # slm / month
                for row in range(12):
                        row_num += 1
                        for col_num in range(2):
                                if col_num == 0:
                                        ws.write(row_num, col_num, list_months[row], font_style)
                                else:
                                        ws.write(row_num, col_num, list_nr[row], font_style)
                row_num +=2
                # team impact
                for row in range(6):
                        row_num += 1
                        for col_num in range(2):
                                if col_num == 0:
                                       ws.write(row_num, col_num, team_impact_name[row], font_style)
                                else:
                                       ws.write(row_num, col_num, team_impact[row], font_style)
                                       
                
                row_num +=2
                ws.write(row_num,0,"ECU",font_style)
                # team impact
                for row in range(len(ecu_name)):
                        row_num += 1
                        for col_num in range(2):
                                if col_num == 0:
                                       ws.write(row_num, col_num, ecu_name[row], font_style)
                                else:
                                       ws.write(row_num, col_num, ecu_nr[row], font_style)                            
                row_num +=2
                ws.write(row_num,0,"SUPPLIER",font_style)
                # team impact
                for row in range(len(supplier_name)):
                        row_num += 1
                        for col_num in range(2):
                                if col_num == 0:
                                       ws.write(row_num, col_num, supplier_name[row], font_style)
                                else:
                                       ws.write(row_num, col_num, supplier_nr[row], font_style)   
                                       
                row_num +=2
                ws.write(row_num,0,"CAR",font_style)
                # team impact
                for row in range(len(car_name)):
                        row_num += 1
                        for col_num in range(2):
                                if col_num == 0:
                                       ws.write(row_num, col_num, car_name[row], font_style)
                                else:
                                       ws.write(row_num, col_num, car_nr[row], font_style)   
                             
                                       
                
                wb.save(response)
                return response
                
                
                
                
        return render(request,"slm_ok_month.html")

class tutorial_upload(CreateView):
    model=tutorial_model
    form=tutorial_form
    fields=('title','version','description_file')
    success_url=reverse_lazy('tutoriallist')
    template_name='tutorial_upload.html'
class tutorial_list(ListView):
    model=tutorial_model
    template_name='tutorial_list.html'
    context_object_name='tutorials'
def tutorial_last(request):
    tutorial= tutorial_model.objects.last() 
    context= {'tutorial': tutorial}    
    return render(request, 'lasttutorial.html', context)
def delete_tutorial(request, id):
    obj=get_object_or_404(tutorial_model, id=id)
    if request.method== 'POST':
        obj.delete()
    return redirect('tutoriallist')

class homepage(TemplateView):
    template_name='homepage.html'

class frontpage(TemplateView):
    template_name='frontpage.html'
# Create your views here.

from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm
class register(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'base2.html'

def verify_user(request):
        users = CustomUser.objects.all()
        context ={
            'users':users
                }
        if request.method=="POST":
                
                ipn = request.POST.get("ipn","")
                #ipn=obj["ipn"]
                print(ipn)
                if ipn is not "":
                        for i in users:
                                if i.username == ipn:
                                        i.verified = True
                                        i.save()
                                        print("DOne")
                print("received")
        return render(request,'verify_user.html',context)

class account_not_verified(TemplateView):
        template_name='account_not_verified.html'
        

