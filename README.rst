.. image:: https://travis-ci.org/arkanister/django-contact-form-site.svg?branch=master
    :target: https://travis-ci.org/arkanister/django-contact-form-site

.. image:: https://img.shields.io/pypi/v/django-contact-form-site.svg
   :target: https://pypi.python.org/pypi/django-contact-form-site

.. image:: https://img.shields.io/pypi/dm/django-contact-form-site.svg
   :target: https://pypi.python.org/pypi/django-contact-form-site
   
.. image:: https://badge.waffle.io/arkanister/django-contact-form-site.svg?label=ready&title=Ready
   :target: https://waffle.io/arkanister/django-contact-form-site
   :alt: 'Stories in Ready' 

Django Contact
==============

An app to manage contact forms to django sites.

Installation
------------

1. Install with pip or easy install (All dependencies will be installed automatically)::

    pip install http://twhiteman.netfirms.com/pyDES/pyDes-2.0.1.zip  # secure engine
    pip install django-contact-form-site

2. Add ``django_contact`` to your INSTALLED_APPS and all the plugins you want, setting like this::

    INSTALLED_APPS = (
        ...

        'django_contact',
    )

3. Define migrations modules. *(Only django >= 1.7)*::

    MIGRATION_MODULES = {
        ...

        'django_contact': 'django_contact.migrations_django',
    }

    urlpatterns = patterns('',
        ......
        (r'^contact/', include('django_contact.urls')),
        ......
    )

4. Run ``python manage.py syncdb`` or ``python manage.py migrate``.

5. Create a contact config in django admin.

6. Be Happy :)