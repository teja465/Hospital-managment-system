# Generated by Django 3.0.8 on 2020-07-11 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_no', models.CharField(max_length=10)),
                ('type', models.IntegerField(choices=[(1, 'Admin'), (2, 'Staff'), (3, 'Doctor')])),
                ('branch_of_user', models.ManyToManyField(to='myapp1.branch_model')),
            ],
        ),
    ]