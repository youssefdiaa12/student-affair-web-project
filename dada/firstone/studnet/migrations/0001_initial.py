# Generated by Django 4.0.4 on 2022-05-24 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='studnet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentname', models.CharField(max_length=50)),
                ('course', models.CharField(max_length=50)),
                ('department', models.CharField(max_length=50)),
                ('student_id', models.CharField(max_length=50)),
                ('gpa', models.DecimalField(decimal_places=2, max_digits=3)),
            ],
        ),
    ]
