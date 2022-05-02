# Generated by Django 3.2.4 on 2022-04-28 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GroupOfUser',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100)),
                ('created', models.DateField(auto_now_add=True)),
                ('group', models.ManyToManyField(to='base.GroupOfUser')),
            ],
        ),
    ]
