# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usr_ant', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PeerGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('groupname', models.CharField(max_length=32)),
                ('peers', models.ManyToManyField(to='usr_ant.Peer')),
            ],
        ),
    ]
