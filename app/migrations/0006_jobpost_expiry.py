# Generated by Django 5.1 on 2024-09-02 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0005_alter_jobpost_slug"),
    ]

    operations = [
        migrations.AddField(
            model_name="jobpost",
            name="expiry",
            field=models.DateField(null=True),
        ),
    ]