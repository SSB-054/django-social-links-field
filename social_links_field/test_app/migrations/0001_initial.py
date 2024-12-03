# Generated by Django 5.1.3 on 2024-12-03 04:42

import social_links_field.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('social_links', social_links_field.models.SocialLinksField(default=list)),
            ],
        ),
    ]
