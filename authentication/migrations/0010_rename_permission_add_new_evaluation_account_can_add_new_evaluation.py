# Generated by Django 4.0.5 on 2022-08-02 12:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0009_alter_account_permission_add_new_evaluation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='permission_add_new_evaluation',
            new_name='can_add_new_evaluation',
        ),
    ]
