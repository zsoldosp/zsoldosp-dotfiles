I wish https://docs.djangoproject.com/en/1.3/topics/db/aggregation/ included https://docs.djangoproject.com/en/1.3/ref/models/querysets/#id8
 distinct=True

i.e.: django equivalent of select count distinct a.k.a. finding duplicates

    >>> from django.contrib.auth.models import User
    >>> from django.db.models import Count
    >>> qs = User.objects.values_list('last_name').annotate(cnt=Count('first_name', distinct=True))
    >>> qs.query
    SELECT `auth_user`.`last_name`, COUNT(DISTINCT `auth_user`.`first_name`) AS `cnt` FROM `auth_user` GROUP BY `auth_user`.`last_name`, `auth_user`.`last_name` ORDER BY NULL
    >>> duplicates = qs.filter(cnt__gte=2)
    >>> duplicates.query
    SELECT `auth_user`.`last_name`, COUNT(DISTINCT `auth_user`.`first_name`) AS `cnt` FROM `auth_user` GROUP BY `auth_user`.`last_name`, `auth_user`.`last_name` HAVING COUNT(DISTINCT `auth_user`.`first_name`) >= 2  ORDER BY NULL
