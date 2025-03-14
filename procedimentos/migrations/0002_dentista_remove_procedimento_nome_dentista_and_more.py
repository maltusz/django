# Generated by Django 5.1.2 on 2024-10-20 14:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('procedimentos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dentista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('telefone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=75)),
                ('cro', models.CharField(max_length=15)),
            ],
        ),
        migrations.RemoveField(
            model_name='procedimento',
            name='nome_dentista',
        ),
        migrations.AddField(
            model_name='procedimento',
            name='dentista',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='procedimentos', to='procedimentos.dentista'),
        ),
    ]
