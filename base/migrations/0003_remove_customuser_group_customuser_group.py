# Generated by Django 4.0.4 on 2022-04-30 16:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_alter_customuser_created'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='group',
        ),
        migrations.AddField(
            model_name='customuser',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.groupofuser'),
        ),
    ]
