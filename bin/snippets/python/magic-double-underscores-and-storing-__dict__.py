class BadWayToDoIt(object):
    def __init__(self):
        self.orig_values = self.__dict__



class GoodWayToDoIt(object):
    def __init__(self):
        d = dict(self.__dict__)
        self.orig_values = d


def assert_equals(expected, actual):
    assert expected == actual, 'Expected %r, but got %r' % (expected, actual)

assert_equals({'orig_values': {}}, GoodWayToDoIt().__dict__)
b = BadWayToDoIt()
assert_equals(b.orig_values, b.orig_values['orig_values']) # inifinite linked list :)


class GoodWayToDoItSingleUnderscore(object):
    def __init__(self):
        self._orig_values = set((k, v) for (k, v) in self.__dict__.iteritems())

class AnotherBadWayToDoItAkaMagicTwoUnderscores(object):
    def __init__(self):
        self.__orig_values = set((k, v) for (k, v) in self.__dict__.iteritems())


assert_equals({'_orig_values': set([])}, GoodWayToDoItSingleUnderscore().__dict__)
assert_equals({'_AnotherBadWayToDoItAkaMagicTwoUnderscores__orig_values': set([])}, AnotherBadWayToDoItAkaMagicTwoUnderscores().__dict__)
