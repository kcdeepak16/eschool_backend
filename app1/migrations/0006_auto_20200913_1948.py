# Generated by Django 3.0.3 on 2020-09-13 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_intern_form_teacher_form'),
    ]

    operations = [
        migrations.AddField(
            model_name='intern_form',
            name='contacted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='teacher_form',
            name='contacted',
            field=models.BooleanField(default=False),
        ),
    ]
