# Generated by Django 4.2.1 on 2023-05-16 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='teacher',
        ),
        migrations.AddField(
            model_name='teacher',
            name='students',
            field=models.ManyToManyField(related_name='teachers', to='school.student', verbose_name='Ученики'),
        ),
    ]