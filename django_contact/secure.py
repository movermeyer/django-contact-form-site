# coding: utf-8
import hashlib
from base64 import b64decode
from django.db import models
from django.utils.translation import ugettext_lazy as _
from pyDes import triple_des, ECB, PAD_PKCS5


class MD5(object):
    """ A class to encrypt and decrypt string in MD5 """
    def __init__(self, hash_key=None):
        self.hash_key = hash_key or '7f715edb8aa6b2834bac979ea172eaf2'

    def __repr__(self):
        return "<MD5: '%s'>" % self.hash_key

    def encrypt(self, value):
        value = str(value)
        _md5 = hashlib.md5()
        _md5.update(self.hash_key)
        k = triple_des(_md5.digest(), ECB, padmode=PAD_PKCS5)
        return k.encrypt(value).encode("base64").rstrip()

    def decrypt(self, value):
        value = b64decode(value)
        _md5 = hashlib.md5()
        _md5.update(self.hash_key)
        k = triple_des(_md5.digest(), ECB, padmode=PAD_PKCS5)
        return k.decrypt(value)


md5 = MD5()


class MD5Field(models.CharField):
    description = _("MD5 String")

    def get_prep_value(self, value):
        value = super(MD5Field, self).get_prep_value(value)
        if value is not None:
            if value.startswith('md5:'):
                return value
            return "md5:" + md5.encrypt(self.to_python(value))
        return value

    def to_python(self, value):
        if value is not None:
            if value.startswith('md5:'):
                value = value.replace("md5:", "")
                value = md5.decrypt(value)
        return value

    def value_from_object(self, obj):
        """
        Returns the value of this field in the given model instance.
        """
        return self.to_python(getattr(obj, self.attname))

    def contribute_to_class(self, cls, name, virtual_only=False):
        super(MD5Field, self).contribute_to_class(cls, name, virtual_only=virtual_only)

        def get_decrypted_from_object(obj):
            value = getattr(obj, name, None)
            if value is None:
                return None
            value = value.replace("md5:", "")
            return md5.decrypt(value)

        setattr(cls, "get_%s_decrypted" % name, get_decrypted_from_object)