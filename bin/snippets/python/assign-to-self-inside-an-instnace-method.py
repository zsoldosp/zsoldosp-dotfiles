class Foo:
    @staticmethod
    def from_db(pk):
        return Foo(pk=pk, state='db')

    def __init__(self, pk, state):
        self.pk = pk
        self.state = state

    def dirty(self, dirty_state):
        self.state = dirty_state

    def reload_from_db_via_assignment(self):
        self = Foo.from_db(self.pk)

    def reload_from_db_via_dict_overwrite(self):
        obj = Foo.from_db(self.pk)
        self.__dict__.update(obj.__dict__)
    
def assert_equal(expected, actual):
    assert expected == actual, 'expected %r, got %r' % (expected, actual)

sut = Foo.from_db(1)
assert_equal('db', sut.state)

sut.dirty('client modified state')
assert_equal ('client modified state', sut.state)

sut.reload_from_db_via_assignment()
assert_equal ('client modified state', sut.state) # surprised, eh?

sut.reload_from_db_via_dict_overwrite()
assert_equal ('db', sut.state) 
