# Generated by Django 2.2.2 on 2019-06-09 12:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('familiar', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='UserStages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stageid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.Stages')),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.Users')),
            ],
        ),
    ]
