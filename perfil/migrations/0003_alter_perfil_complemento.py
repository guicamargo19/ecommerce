# Generated by Django 5.0.3 on 2024-03-20 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0002_alter_perfil_cep_alter_perfil_cpf_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='complemento',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
