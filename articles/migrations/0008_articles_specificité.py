# Generated by Django 5.1.1 on 2024-09-10 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_alter_annonces_titre'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='specificité',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
