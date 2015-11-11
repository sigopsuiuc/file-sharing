# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usr_ant', '0002_peergroup'),
    ]

    operations = [
        migrations.AddField(
            model_name='peer',
            name='ip_addr',
            field=models.GenericIPAddressField(default=b'127.0.0.1'),
        ),
        migrations.AddField(
            model_name='peer',
            name='port',
            field=models.IntegerField(default=5005),
        ),
    ]
