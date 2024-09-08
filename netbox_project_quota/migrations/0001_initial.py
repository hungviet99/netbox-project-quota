# Generated by Django 5.0.6 on 2024-08-23 15:23

import django.db.models.deletion
import taggit.managers
import utilities.json
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dcim', '0187_alter_device_vc_position'),
        ('extras', '0115_convert_dashboard_widgets'),
        ('ipam', '0069_gfk_indexes'),
        ('tenancy', '0015_contactassignment_rename_content_type'),
        ('virtualization', '0038_virtualdisk'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuotaTemplate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict, encoder=utilities.json.CustomFieldJSONEncoder)),
                ('template_name', models.CharField(max_length=100, null=True)),
                ('instances_quota', models.PositiveIntegerField(null=True)),
                ('vcpus_quota', models.PositiveIntegerField(null=True)),
                ('ram_quota', models.PositiveIntegerField(null=True)),
                ('ipaddr_quota', models.PositiveIntegerField(null=True)),
                ('device_quota', models.PositiveIntegerField(null=True)),
                ('comments', models.TextField(blank=True)),
                ('tags', taggit.managers.TaggableManager(through='extras.TaggedItem', to='extras.Tag')),
            ],
            options={
                'ordering': ('template_name',),
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict, encoder=utilities.json.CustomFieldJSONEncoder)),
                ('name', models.CharField(max_length=100)),
                ('project_id', models.CharField(blank=True, max_length=100)),
                ('status', models.CharField(max_length=30)),
                ('description', models.CharField(blank=True, max_length=500)),
                ('device_count', models.IntegerField(blank=True, default=None, null=True)),
                ('ip_count', models.IntegerField(blank=True, default=None, null=True)),
                ('vm_count', models.IntegerField(blank=True, default=None, null=True)),
                ('user_count', models.IntegerField(blank=True, default=None, null=True)),
                ('ram_quota_used', models.CharField(default=None, max_length=100, null=True)),
                ('cpu_quota_used', models.CharField(default=None, max_length=100, null=True)),
                ('disk_quota_used', models.CharField(default=None, max_length=100, null=True)),
                ('device_quota_used', models.CharField(default=None, max_length=100, null=True)),
                ('vm_quota_used', models.CharField(default=None, max_length=100, null=True)),
                ('ip_quota_used', models.CharField(default=None, max_length=100, null=True)),
                ('comments', models.TextField(blank=True)),
                ('contact', models.ManyToManyField(blank=True, default=None, related_name='assigned_contact', to='tenancy.contact')),
                ('devices', models.ManyToManyField(blank=True, default=None, related_name='assigned_device', to='dcim.device')),
                ('ipaddress', models.ManyToManyField(blank=True, default=None, related_name='assigned_ipaddress', to='ipam.ipaddress')),
                ('project_owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tenancy.contact')),
                ('tags', taggit.managers.TaggableManager(through='extras.TaggedItem', to='extras.Tag')),
                ('virtualmachine', models.ManyToManyField(blank=True, default=None, related_name='assigned_vm', to='virtualization.virtualmachine')),
                ('quota_template', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='project_quota', to='netbox_project_quota.quotatemplate')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]
