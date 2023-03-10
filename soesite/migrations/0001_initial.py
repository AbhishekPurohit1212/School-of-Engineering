# Generated by Django 3.2.5 on 2021-11-10 22:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='branch',
            fields=[
                ('branch_id', models.IntegerField(primary_key=True, serialize=False)),
                ('branch_name', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='subject',
            fields=[
                ('subject_id', models.IntegerField(primary_key=True, serialize=False)),
                ('quiz_link', models.CharField(max_length=300)),
                ('subject_name', models.CharField(max_length=100)),
                ('year_id', models.IntegerField()),
                ('branch_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='soesite.branch')),
            ],
        ),
        migrations.CreateModel(
            name='resource',
            fields=[
                ('resource_id', models.IntegerField(primary_key=True, serialize=False)),
                ('resource_link', models.CharField(max_length=300)),
                ('resource_type', models.CharField(max_length=30)),
                ('resource_name', models.CharField(max_length=200, null=True)),
                ('subject_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='soesite.subject')),
            ],
        ),
    ]
