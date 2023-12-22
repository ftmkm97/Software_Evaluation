# Generated by Django 4.0.5 on 2022-08-03 09:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('metric_evaluation', '0002_alter_metricevaluate_completed_datetime_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('compare_evaluation', '0002_alter_compareevaluate_completed_datetime_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompareEvaluateValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main', models.PositiveIntegerField()),
                ('target', models.PositiveIntegerField()),
                ('parameter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='metric_evaluation.metricparameter')),
            ],
        ),
        migrations.CreateModel(
            name='CompareEvaluateResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('evaluate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='compare_evaluation.compareevaluate')),
                ('evaluated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('result', models.ManyToManyField(blank=True, to='compare_evaluation.compareevaluatevalue')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
