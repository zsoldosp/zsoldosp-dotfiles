def return_in_finally_overwrites_return_in_except():
    try:
        raise Exception('exception from try')
    except:
        return 'except'
    finally:
        return 'finally'


assert 'finally' == return_in_finally_overwrites_return_in_except(), return_in_finally_overwrites_return_in_except()
