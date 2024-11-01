# Generated by Django 5.1.2 on 2024-11-01 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Feedback', '0005_alter_feedback_avalição'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='avalição',
        ),
        migrations.AddField(
            model_name='feedback',
            name='avaliacao',
            field=models.CharField(choices=[('POSITIVO', 'Positivo'), ('NEGATIVO', 'Negativo'), ('SUGESTAO', 'Sugestão')], default='Positivo', max_length=10),
        ),
    ]
