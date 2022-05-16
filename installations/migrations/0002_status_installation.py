# Generated by Django 4.0.3 on 2022-05-15 14:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('installations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='status',
            name='installation',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='status', to='installations.installation'),
            preserve_default=False,
        ),
    ]
