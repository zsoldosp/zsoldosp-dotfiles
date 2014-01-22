class First(object):
    index = 1


class Second(object):
    index = 2


class Red(object):
    color = 'red'


class Blue(object):
    color = 'blue'


import sys


def runwith(*classes):
    """
    Unconditionally skip a test.
    """
    def decorator(target_cls):
        for mixin_cls in classes:
            class Combo(mixin_cls, target_cls):
                pass
            Combo.__name__ = ''.join([mixin_cls.__name__, target_cls.__name__])
            setattr(sys.modules[target_cls.__module__], Combo.__name__, Combo)
        return target_cls
    return decorator


@runwith(First, Second)
class Foo(object):
    def data(self):
        return (self.index, type(self))


print SecondFoo().data()



