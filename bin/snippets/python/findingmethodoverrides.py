class BaseClass(object):
    def is_foo(self):
        return True

class MiddleClass(BaseClass):
    pass

class Mixin(object):
    pass

class BottomClass(MiddleClass, Mixin):
    def is_foo(self):
        return False

def get_method_definitions(base_class, method_name):
    actual_definitions = []
    for cls in reversed(base_class.__mro__):
        if not hasattr(cls, method_name):
            continue
        if len(actual_definitions) == 0:
            actual_definitions.append(cls)
        last_seen = actual_definitions[-1]
        if getattr(last_seen, method_name).__func__ != getattr(cls, method_name).__func__:
            actual_definitions.append(cls)
    return actual_definitions

print 'actual method definitions', get_method_definitions(BottomClass, 'is_foo')
