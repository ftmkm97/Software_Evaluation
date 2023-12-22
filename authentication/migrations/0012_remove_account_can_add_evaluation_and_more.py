# Generated by Django 4.0.5 on 2022-08-02 13:20

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0011_remove_account_can_add_new_evaluation_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='can_add_evaluation',
        ),
        migrations.AddField(
            model_name='account',
            name='can_publish_evaluation',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('metric', 'Metric'), ('comment', 'Comment'), ('rating', 'Rating'), ('compare', 'Compare'), ('questionnaire', 'Questionnaire')], default=['metric', 'comment', 'rating', 'compare', 'questionnaire'], max_length=43, null=True, verbose_name='Publish evaluation'),
        ),
    ]
