# Generated by Django 3.0.6 on 2020-06-20 08:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='construction',
            name='parent',
        ),
        migrations.AddField(
            model_name='construction',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='website.ConstructionBanner'),
        ),
    ]
