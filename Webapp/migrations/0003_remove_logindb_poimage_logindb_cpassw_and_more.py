# Generated by Django 5.0.6 on 2024-05-29 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Webapp', '0002_logindb'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='logindb',
            name='Poimage',
        ),
        migrations.AddField(
            model_name='logindb',
            name='Cpassw',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='logindb',
            name='Passw',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
