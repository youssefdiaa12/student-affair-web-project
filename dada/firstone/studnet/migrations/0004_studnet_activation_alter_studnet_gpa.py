# Generated by Django 4.0.4 on 2022-05-25 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studnet', '0003_alter_studnet_gpa'),
    ]

    operations = [
        migrations.AddField(
            model_name='studnet',
            name='activation',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='studnet',
            name='gpa',
            field=models.CharField(max_length=3),
        ),
    ]
