class First(object):
    index = 1


class Second(object):
    index = 2


class Red(object):
    color = 'red'


class Blue(object):
    color = 'blue'


import sys
import itertools


def runwith(*class_combinations):

    def to_class(existing, new):
        class Tmp(existing, new):
            pass
        Tmp.__name__ = ''.join([existing.__name__, new.__name__])
        return Tmp


    def flatten(listOfLists):
        "Flatten one level of nesting"
        return itertools.chain.from_iterable(listOfLists)

            

    def decorator(target_cls):
        outstanding = list(class_combinations)
        existing = [target_cls]
        while outstanding:
            curr = outstanding.pop()
            existing = list(
                to_class(c, e)
                for e in existing
                for c in curr
            )
        for cls in existing:
            setattr(sys.modules[target_cls.__module__], cls.__name__, cls)
        return target_cls

    return decorator


@runwith(
    (First, Second),
    (Red, Blue),
)
class Demo(object):
    def data(self):
        return (self.index, self.color, type(self))


print SecondRedDemo().data()



