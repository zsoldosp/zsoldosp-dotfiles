from django.contrib.auth.models import User

def multireduce(original_qs, *model_to_m2m_functions):
    result = original_qs
    for model_to_m2m in model_to_m2m_functions:
        result = reduce(lambda left, obj: left + list(model_to_m2m(obj)), result, [])
    return result

# this is especially helpful when working with generic foreign keys
print set(multireduce(
    User.objects.filter(email__endswith='mycompany.com'), 
    lambda user: user.groups.all(), 
    lambda group: group.permissions.all()
))
