# Generated by Django 4.2.5 on 2023-10-04 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_investor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investor',
            name='created_by',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='investor',
            name='image_id',
            field=models.ImageField(upload_to='images'),
        ),
    ]