# Generated by Django 4.0.4 on 2022-05-25 18:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('studnet', '0006_alter_studnet_gpa'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studnet',
            name='mob',
        ),
        migrations.AddField(
            model_name='studnet',
            name='level',
            field=models.CharField(default=django.utils.timezone.now, max_length=1),
            preserve_default=False,
        ),
    ]