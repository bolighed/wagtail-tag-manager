# Generated by Django 2.2.5 on 2019-09-11 13:16

import uuid

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtail_tag_manager', '0014_auto_20190911_1116'),
    ]

    operations = [
        migrations.CreateModel(
            name='CookieConsent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('consent_state', models.TextField(editable=False)),
                ('location', models.URLField(editable=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]