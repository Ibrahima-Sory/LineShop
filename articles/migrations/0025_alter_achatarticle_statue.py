# Generated by Django 5.1.1 on 2024-09-20 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0024_alter_achatarticle_numero'),
    ]

    operations = [
        migrations.AlterField(
            model_name='achatarticle',
            name='statue',
            field=models.CharField(choices=[('En attente', 'En attente'), ('Confirmé', 'Confirmé'), ('Livré', 'Livré')], default='En attente', max_length=50),
        ),
    ]
