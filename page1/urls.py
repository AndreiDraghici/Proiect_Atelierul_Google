from django.urls import include,path
from . import views

from .views import  CustomLoginView,register,slmregister,homepage,frontpage,superuser,slm_request_detail,superusermenu,delete_tutorial,history,changeipn
from .views import slm_request_detail,tutorial_upload,tutorial_list,tutorial_last, make_specialist,remove_specialist, specialist_menu, slm_number_detail, components_review 
from .views import circuit_review, enviro_review, process_review, emc_review
from .views import make_superuser, history_slm, verify_user, account_not_verified, changecuet, suivi, slm_done
from .views import export_suivi_xls, export_karte_pdf, statistics, users_and_staff, remove_superuser,history_all, history_slm_all
urlpatterns = [
    path('',frontpage.as_view(), name='frontpage'),
    path('register/',register.as_view(),name='register'),
    path('slmreg/',slmregister,name='slmregister'),
    path('list/',tutorial_list.as_view(),name='tutoriallist'),
    path('list/upload/',tutorial_upload.as_view(),name='tutorialupload'),
    path('login/tutorial/',tutorial_last,name='tutorialpde'),
    path('list/<int:id>/',delete_tutorial,name='delete_tutorial'),
    path('homepage/',homepage.as_view(),name='homepage'),
    path('login/',CustomLoginView.as_view(),name='login'), 
    path('superuser/',superuser,name='superuser'),
    path('menu/',superusermenu.as_view(),name='menu'),
    path('<int:id>',slm_request_detail.as_view(),name='detail'),
    path('move_not_ok',slm_request_detail.notok),
    path('move_ok',slm_request_detail.ok),
    path('history/',history,name='history'),
    path('history_all/',history_all,name="history_all"),
    path('history_all/history_slm_all',history_slm_all,name='history_slm_all'),   
    path('history/history_slm',history_slm,name='history_slm'),
    #path('check_specialist_slm/',check_specialist_slm,name='check_specialist_slm'),
    path('changeipn/',changeipn,name='changeipn'),
    path('changecuet/',changecuet,name='changecuet'),
    path('specialist_menu/',specialist_menu,name='specialist_menu'),
    path('components',slm_number_detail.components),
    path('components_review',components_review,name='components_review'),
    path('circuit',slm_number_detail.circuit),
    path('circuit_review',circuit_review,name='circuit_review'),
    path('enviro',slm_number_detail.enviro),
    path('enviro_review',enviro_review,name='enviro_review'),
    path('process',slm_number_detail.process),
    path('process_review',process_review,name='process_review'),
    path('emc',slm_number_detail.emc),
    path('emc_review',emc_review,name='emc_review'),
    path('<str:slm_number>',slm_number_detail.as_view(),name='slm_number'),
   # path('harware_<str:slm_number>',slm_hard,name='slm_hard'),
    path('make_specialist/',make_specialist,name='make_specialist'),
    path('remove_specialist/',remove_specialist,name='remove_specialist'),
    path('make_superuser/',make_superuser,name='make_superuser'),
    path('remove_superuser/',remove_superuser,name='remove_superuser'),
    path('verify_user/',verify_user,name='verify_user'),
    path('account_not_verified/',account_not_verified.as_view(),name='account_not_verified'),
    path('suivi/',suivi,name='suivi'),
    path('slm_done/',slm_done, name='slm_done'),
    path(r'^export/xls/$', views.export_suivi_xls, name='export_suivi_xls'),
    #url(r'^export/pdf/$',views.export_karte_pdf,name='export_karte_pdf'),
    path('export/pdf/',export_karte_pdf,name='export_karte_pdf'),
    path('statistics/',statistics,name='statistics'),
    path('users_and_staff/',users_and_staff,name='users_and_staff')
    
    ]
