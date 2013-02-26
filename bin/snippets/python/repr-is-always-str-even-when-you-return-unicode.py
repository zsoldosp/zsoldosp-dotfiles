# ah, the niceties of python. One way, and no surprises
class Foo:
    def __init__(self, val):
        self.val = val

    def __unicode__(self):
        return unicode(self.val)

    def __repr__(self):
        return unicode(self)


foo = Foo('somestring')

assert unicode == type(foo.__repr__()), 'calling it directly behaves as expected, i.e.: it is %s' % type(foo.__repr__())
assert unicode == type(repr(foo)), 'in for a surprise, this will raise an error, because  type is %s' % type(repr(foo))

# all I can offer for explanation is http://docs.python.org/2.6/reference/datamodel.html?highlight=__repr__#object.__repr__
# [...] The return value must be a string object [...]
