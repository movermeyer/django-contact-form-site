# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_contact.secure


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactForm',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='Name to identify the contact form.', max_length=100)),
                ('slug', models.SlugField(help_text="Unique name to retrieve the form in rendering the tag 'show_contact_form'.", unique=True, max_length=100)),
                ('form', models.CharField(default=b'django_contact.forms.ContactForm', help_text='Form the class path to be used when sending contact.', max_length=255, choices=[(b'django_contact.forms.ContactForm', 'Default form')])),
                ('auth_email_user', models.EmailField(default=b'no-reply@incloudsolutions.com.br', help_text='User to authenticate to the SMTP server.', max_length=75)),
                ('auth_email_password', django_contact.secure.MD5Field(help_text='Password to authenticate to the SMTP server.', max_length=50)),
                ('auth_email_host', models.CharField(help_text='Host SMTP authentication server.', max_length=50)),
                ('auth_email_port', models.PositiveIntegerField(default=587, help_text='Port SMTP authentication server. Default 3306.')),
                ('auth_email_use_tls', models.BooleanField(default=False, help_text='The SMTP server uses TLS (Transport Layer Security).')),
                ('recipient_list', models.CharField(help_text="E-mail list that will receive the contact. Separated by ','.", max_length=2048)),
                ('email_subject', models.CharField(help_text=b'Title the email that will be sent.', max_length=255)),
                ('email_html_content', models.TextField(help_text='HTML content of the email being sent.')),
                ('email_text_content', models.TextField(help_text='Plain Text content of the email being sent.')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
