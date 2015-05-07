# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_contact.secure


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactConfig',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sent_url_redirect', models.CharField(default=b'/', help_text='Redirect page after sending the email. Only to non-ajax requests.', max_length=255)),
                ('auth_email_user', models.EmailField(help_text='User to authenticate to the SMTP server.', max_length=75)),
                ('auth_email_password', django_contact.secure.MD5Field(help_text='Password to authenticate to the SMTP server.', max_length=50)),
                ('auth_email_host', models.CharField(help_text='Host SMTP authentication server.', max_length=50)),
                ('auth_email_port', models.PositiveIntegerField(default=3306, help_text='Port SMTP authentication server. Default 3306.')),
                ('auth_email_use_tls', models.BooleanField(default=False, help_text='The SMTP server uses TLS (Transport Layer Security).')),
                ('recipient_list', models.CharField(help_text="E-mail list that will receive the contact. Separated by ','.", max_length=2048)),
                ('email_subject', models.CharField(help_text=b'Title the email that will be sent.', max_length=255)),
                ('email_html_content', models.TextField(help_text='HTML content of the email being sent.')),
                ('email_text_content', models.TextField(help_text='Plain Text content of the email being sent.')),
            ],
            options={
                'verbose_name': 'Contact Config',
                'verbose_name_plural': 'Contacts Config',
            },
            bases=(models.Model,),
        ),
    ]
