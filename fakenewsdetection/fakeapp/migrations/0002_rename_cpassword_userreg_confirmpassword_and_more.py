# Generated by Django 4.2.11 on 2024-09-28 07:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fakeapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userreg',
            old_name='cpassword',
            new_name='ConfirmPassword',
        ),
        migrations.RenameField(
            model_name='userreg',
            old_name='email',
            new_name='Email',
        ),
        migrations.RenameField(
            model_name='userreg',
            old_name='gender',
            new_name='Gender',
        ),
        migrations.RenameField(
            model_name='userreg',
            old_name='password',
            new_name='Password',
        ),
    ]
