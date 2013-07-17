from django.db.models import signals
from django.conf import settings
import os
import warnings

def raise_warnings_if_signal_based_registration_pre_requisites_are_not_met():
    if __package__ not in settings.INSTALLED_APPS:
        warnings.warn('%s is not present in settings.INSTALLED_APPS, thus its models are not available' % __package__)
    elif settings.INSTALLED_APPS.index(__package__) != 0:
        warnings.warn('%s is not the first in settings.INSTALLED_APPS, thus any models from prior application will not be inspected/registered' % __package__)

has_warned = False
try:
    settings.REGISTER_VIA_SIGNALS
except AttributeError:
    settings.REGISTER_VIA_SIGNALS = False
    

def model_registered(signal = None, sender = None, **kwargs):
    print 'here I will do custom inspection and registration for model %s' % sender
    
if settings.REGISTER_VIA_SIGNALS:
    if not has_warned:
        raise_warnings_if_signal_based_registration_pre_requisites_are_not_met()
        signals.class_prepared.connect(model_registered)
        has_warned = True

