
# https://pythonconquerstheuniverse.wordpress.com/2012/02/15/mutable-default-arguments/
def foobar(arg_list = []): 
    arg_list.append("F")
    return arg_list
 
for i in range(4): 
    assert len(foobar()) == 1, 'at value %d of i, presumption fails about default arguments' % i
