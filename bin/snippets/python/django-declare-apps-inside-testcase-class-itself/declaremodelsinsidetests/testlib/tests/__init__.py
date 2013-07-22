from django.test import TestCase
from django.db import models 
from django.conf import settings
import sys

LIBRARY_NAME = 'testlib'

class ModelsAreRegisteredWhenDeclared(TestCase):
    def setUp(self):
        super(ModelsAreRegisteredWhenDeclared, self).setUp()
        self.original_model_classes = set(models.get_models())
        
    def test_model_registered_when_declared(self):
        class FooModel(models.Model):
            pass
        models_after_declaring_class = set(models.get_models())
        self.assertEquals(len(self.original_model_classes) + 1, len(models_after_declaring_class))
        self.assertEquals(set([FooModel]), models_after_declaring_class - self.original_model_classes)

    def test_app_label_is_by_default_derives_from_module_regardsless_of_class_level_nesting(self):
        cls2app_label = lambda cls: sys.modules[cls.__module__].__name__.split('.')[-2]
        self.assertEquals(LIBRARY_NAME, cls2app_label(ModelsAreRegisteredWhenDeclared), 'if the test helper lambda does not work, no point proceeding further')
        class NotNested(models.Model):
            pass
        self.assertEquals(cls2app_label(ModelsAreRegisteredWhenDeclared), NotNested()._meta.app_label)
        class appname:
            class models:
                class NestedModel(models.Model):
                    pass
        self.assertEquals(cls2app_label(ModelsAreRegisteredWhenDeclared), appname.models.NestedModel()._meta.app_label)

    def test_app_label_can_be_overwritten_via_signal(self):
        def overwrite_app_label(signal, sender):
            new_model_cls = sender
            new_model_cls._meta.app_label = 'overwrittenapplabel'
        models.signals.class_prepared.connect(overwrite_app_label)
        try:
            class WillGetCustomAppLabel(models.Model):
                pass
            self.assertEquals('overwrittenapplabel', WillGetCustomAppLabel()._meta.app_label)
            self.assertEquals(WillGetCustomAppLabel, models.get_model('overwrittenapplabel', 'WillGetCustomAppLabel', False))
        finally:
            models.signals.class_prepared.disconnect(overwrite_app_label)
