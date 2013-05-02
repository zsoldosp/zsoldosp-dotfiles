import sys

def orginal_reraised_storing():
    try:
        raise Exception('outer')
    except:
        tp, msg, trace = sys.exc_info()
        try:
            raise Exception('nested')
        except:
            pass
        raise tp, msg, trace

def nested_reraised():
    try:
        raise Exception('outer')
    except:
        try:
            raise Exception('nested')
        except:
            pass
        raise 


#nested_reraised()
#orginal_reraised_storing()
