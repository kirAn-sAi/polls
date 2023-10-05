# Generated by Django 4.2.5 on 2023-10-04 11:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('base_country', models.CharField(max_length=25)),
                ('office_locations', models.IntegerField(default=1)),
                ('domain', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('N', 'Non Binary')], default='M', max_length=1)),
                ('nationality', models.CharField(max_length=50)),
                ('experience', models.IntegerField(default=0)),
                ('skills', models.CharField(max_length=500)),
                ('org', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='polls.organization')),
            ],
        ),
    ]
