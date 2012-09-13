from django.utils.module_loading import module_has_submodule
from django.utils.importlib import import_module
from itertools import chain


def all_subclasseses_of(sub_app_module_name, class_to_implement):
    submodules = filter(
        lambda mod: module_has_submodule(mod, sub_app_module_name),
        map(
            import_module,
            settings.INSTALLED_APPS
        )
    )

    print filter(
        lambda x: type(x) == type and issubclass(x, class_to_implement) and x != class_to_implement,
        chain(*(a.emails.__dict__.values() for a in submodules))
    )
