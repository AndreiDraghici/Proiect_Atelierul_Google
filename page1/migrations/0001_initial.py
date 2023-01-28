# Generated by Django 3.0.4 on 2020-06-19 06:22

import django.contrib.auth.models
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='slm_request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(blank=True, max_length=100, null=True)),
                ('responsible', models.CharField(blank=True, max_length=100, null=True)),
                ('cuet', models.CharField(max_length=100)),
                ('cuet_IPN', models.CharField(max_length=100)),
                ('budget', models.CharField(max_length=100)),
                ('ecu', models.CharField(max_length=100)),
                ('supplier', models.CharField(max_length=100)),
                ('system', models.CharField(max_length=100)),
                ('asil_lvl', models.CharField(max_length=100)),
                ('pcb_coating', models.CharField(max_length=100)),
                ('current_pcb_plant', models.CharField(max_length=100)),
                ('pcb_assembly_plant_transfer', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
                ('description_file', models.FileField(blank=True, null=True, upload_to='Description/')),
                ('f4_sheet_sent', models.CharField(max_length=100)),
                ('f4_sheet_sent_file', models.FileField(blank=True, null=True, upload_to='F4sheets/')),
                ('leading_vehicle_project', models.CharField(max_length=100)),
                ('leading_vehicle_MA_DATE', models.CharField(max_length=100)),
                ('application_date', models.CharField(max_length=100)),
                ('carry_over', models.CharField(max_length=100)),
                ('lup_number', models.CharField(max_length=100)),
                ('proof_RNPO', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='slm_request_ok',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(blank=True, max_length=100, null=True)),
                ('responsible', models.CharField(blank=True, max_length=100, null=True)),
                ('cuet', models.CharField(max_length=100)),
                ('cuet_IPN', models.CharField(max_length=100)),
                ('budget', models.CharField(max_length=100)),
                ('ecu', models.CharField(max_length=100)),
                ('supplier', models.CharField(max_length=100)),
                ('system', models.CharField(max_length=100)),
                ('asil_lvl', models.CharField(max_length=100)),
                ('pcb_coating', models.CharField(max_length=100)),
                ('current_pcb_plant', models.CharField(max_length=100)),
                ('pcb_assembly_plant_transfer', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('description_file', models.FileField(blank=True, null=True, upload_to='Description/')),
                ('f4_sheet_sent', models.CharField(max_length=100)),
                ('f4_sheet_sent_file', models.FileField(blank=True, null=True, upload_to='F4sheets/')),
                ('leading_vehicle_project', models.CharField(max_length=100)),
                ('leading_vehicle_MA_DATE', models.CharField(max_length=100)),
                ('application_date', models.CharField(max_length=100)),
                ('carry_over', models.CharField(max_length=100)),
                ('lup_number', models.CharField(max_length=100)),
                ('proof_RNPO', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
                ('date', models.DateField(auto_now_add=True)),
                ('date_close', models.DateField(blank=True)),
                ('slm_number', models.CharField(max_length=100)),
                ('comp_status', models.CharField(default='Not Complete', max_length=100)),
                ('comp_change_request', models.CharField(blank=True, max_length=1000, null=True)),
                ('comp_change_request_status', models.CharField(blank=True, max_length=1000, null=True)),
                ('comp_delta', models.CharField(blank=True, max_length=1000, null=True)),
                ('comp_delta_status', models.CharField(blank=True, max_length=1000, null=True)),
                ('comp_updated', models.CharField(blank=True, max_length=1000, null=True)),
                ('comp_updated_status', models.CharField(blank=True, max_length=1000, null=True)),
                ('comp_responsible', models.CharField(blank=True, max_length=100, null=True)),
                ('comp_time', models.CharField(blank=True, default='0', max_length=100, null=True)),
                ('circuit_status', models.CharField(default='Not Complete', max_length=100)),
                ('circuit_schematics', models.CharField(blank=True, max_length=1000, null=True)),
                ('circuit_schematics_status', models.CharField(blank=True, max_length=1000, null=True)),
                ('circuit_delta_bom', models.CharField(blank=True, max_length=1000, null=True)),
                ('circuit_delta_bom_status', models.CharField(blank=True, max_length=1000, null=True)),
                ('circuit_configuration', models.CharField(blank=True, max_length=1000, null=True)),
                ('circuit_configuration_status', models.CharField(blank=True, max_length=1000, null=True)),
                ('circuit_interface', models.CharField(blank=True, max_length=1000, null=True)),
                ('circuit_interface_status', models.CharField(blank=True, max_length=1000, null=True)),
                ('circuit_hardware_design', models.CharField(blank=True, max_length=1000, null=True)),
                ('circuit_hardware_design_status', models.CharField(blank=True, max_length=1000, null=True)),
                ('circuit_component_derating', models.CharField(blank=True, max_length=1000, null=True)),
                ('circuit_component_derating_status', models.CharField(blank=True, max_length=1000, null=True)),
                ('circuit_abnormal_current', models.CharField(blank=True, max_length=1000, null=True)),
                ('circuit_abnormal_current_status', models.CharField(blank=True, max_length=1000, null=True)),
                ('circuit_responsible', models.CharField(blank=True, max_length=100, null=True)),
                ('circuit_time', models.CharField(blank=True, max_length=1000, null=True)),
                ('enviro_status', models.CharField(default='Not Complete', max_length=100)),
                ('enviro_mounting', models.CharField(blank=True, max_length=1000, null=True)),
                ('enviro_mounting_status', models.CharField(blank=True, max_length=1000, null=True)),
                ('enviro_reliability', models.CharField(blank=True, max_length=1000, null=True)),
                ('enviro_reliability_status', models.CharField(blank=True, max_length=1000, null=True)),
                ('enviro_test_reports', models.CharField(blank=True, max_length=1000, null=True)),
                ('enviro_test_reports_status', models.CharField(blank=True, max_length=1000, null=True)),
                ('enviro_responsible', models.CharField(blank=True, max_length=100, null=True)),
                ('enviro_time', models.CharField(blank=True, max_length=100, null=True)),
                ('process_status', models.CharField(default='Not Complete', max_length=100)),
                ('process_peses', models.CharField(blank=True, max_length=1000, null=True)),
                ('process_peses_status', models.CharField(blank=True, max_length=1000, null=True)),
                ('process_cutting_edge', models.CharField(blank=True, max_length=1000, null=True)),
                ('process_cutting_edge_status', models.CharField(blank=True, max_length=1000, null=True)),
                ('process_support_activities', models.CharField(blank=True, max_length=1000, null=True)),
                ('process_support_activities_status', models.CharField(blank=True, max_length=1000, null=True)),
                ('process_spp_activities', models.CharField(blank=True, max_length=1000, null=True)),
                ('process_spp_activities_status', models.CharField(blank=True, max_length=1000, null=True)),
                ('process_off_tool', models.CharField(blank=True, max_length=1000, null=True)),
                ('process_off_tool_status', models.CharField(blank=True, max_length=1000, null=True)),
                ('process_qualification_review', models.CharField(blank=True, max_length=1000, null=True)),
                ('process_qualification_review_status', models.CharField(blank=True, max_length=1000, null=True)),
                ('process_responsible', models.CharField(blank=True, max_length=100, null=True)),
                ('process_time', models.CharField(blank=True, max_length=100, null=True)),
                ('emc_status', models.CharField(default='Not Complete', max_length=100)),
                ('emc_equipment_test_plan', models.CharField(blank=True, max_length=1000, null=True)),
                ('emc_equipment_test_plan_status', models.CharField(blank=True, max_length=1000, null=True)),
                ('emc_equipment_test_reports', models.CharField(blank=True, max_length=1000, null=True)),
                ('emc_equipment_test_reports_status', models.CharField(blank=True, max_length=1000, null=True)),
                ('emc_vehicle_test', models.CharField(blank=True, max_length=1000, null=True)),
                ('emc_vehicle_test_status', models.CharField(blank=True, max_length=1000, null=True)),
                ('emc_existing_deviations', models.CharField(blank=True, max_length=1000, null=True)),
                ('emc_existing_deviations_status', models.CharField(blank=True, max_length=1000, null=True)),
                ('emc_responsible', models.CharField(blank=True, max_length=100, null=True)),
                ('emc_time', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='slm_request_rejected',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(blank=True, max_length=100, null=True)),
                ('responsible', models.CharField(blank=True, max_length=100, null=True)),
                ('cuet', models.CharField(max_length=100)),
                ('cuet_IPN', models.CharField(max_length=100)),
                ('budget', models.CharField(max_length=100)),
                ('ecu', models.CharField(max_length=100)),
                ('supplier', models.CharField(max_length=100)),
                ('system', models.CharField(max_length=100)),
                ('asil_lvl', models.CharField(max_length=100)),
                ('pcb_coating', models.CharField(max_length=100)),
                ('current_pcb_plant', models.CharField(max_length=100)),
                ('pcb_assembly_plant_transfer', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('description_file', models.FileField(blank=True, null=True, upload_to='Description/')),
                ('f4_sheet_sent', models.CharField(max_length=100)),
                ('f4_sheet_sent_file', models.FileField(blank=True, null=True, upload_to='F4sheets/')),
                ('leading_vehicle_project', models.CharField(max_length=100)),
                ('leading_vehicle_MA_DATE', models.CharField(max_length=100)),
                ('application_date', models.CharField(max_length=100)),
                ('carry_over', models.CharField(max_length=100)),
                ('lup_number', models.CharField(max_length=100)),
                ('proof_RNPO', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
                ('date', models.DateField(auto_now_add=True)),
                ('reason', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='tutorial_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('version', models.CharField(max_length=100, verbose_name='Version')),
                ('date', models.DateField(auto_now_add=True)),
                ('description_file', models.FileField(upload_to='Tutorial/')),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.TextField(unique=True, verbose_name='IPN')),
                ('Name', models.TextField(blank=True, null=True)),
                ('email', models.TextField(blank=True, null=True, unique=True, verbose_name='E-mail')),
                ('teamname', models.TextField(blank=True, null=True, verbose_name='Team Name')),
                ('department', models.TextField(blank=True, null=True)),
                ('teamleadername', models.TextField(blank=True, null=True, verbose_name='Team Leader Name')),
                ('departmentleadername', models.TextField(blank=True, null=True, verbose_name='Department Leader Name')),
                ('is_staff', models.BooleanField(default=False)),
                ('Superuser_status', models.BooleanField(default=False)),
                ('verified', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
