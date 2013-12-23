from django.db import models

class SomeModel(models.Model):
    class Meta:
        db_table = 'some_model'

    username = models.CharField(max_length=200)
    domain = models.CharField(max_length=200)


def assert_query_is(expected, queryset):
    actual = str(queryset.query)
    failure_msg = 'Expected %r, got %r' % (expected, actual)
    assert expected == actual, failure_msg


assert_query_is( 'SELECT `some_model`.`id`, `some_model`.`username`, `some_model`.`domain` FROM `some_model`'
, SomeModel.objects.all())

only_google = SomeModel.objects.filter(domain='google.com')
assert_query_is('SELECT `some_model`.`id`, `some_model`.`username`, `some_model`.`domain` FROM `some_model` WHERE `some_model`.`domain` = google.com '
, only_google)
only_microsoft = SomeModel.objects.filter(domain='microsoft.com')
assert_query_is('SELECT `some_model`.`id`, `some_model`.`username`, `some_model`.`domain` FROM `some_model` WHERE `some_model`.`domain` = microsoft.com '
, only_microsoft)

google_or_microsoft = only_google|only_microsoft
assert_query_is('SELECT `some_model`.`id`, `some_model`.`username`, `some_model`.`domain` FROM `some_model` WHERE (`some_model`.`domain` = google.com  OR `some_model`.`domain` = microsoft.com )',  google_or_microsoft)

only_multi_user_domains = SomeModel.objects.values_list('domain').annotate(cnt=models.Count('username', distinct=True)).exclude(cnt__lte=1).values_list('domain', flat=True)
assert_query_is( 'SELECT `some_model`.`domain` FROM `some_model` GROUP BY `some_model`.`domain`, `some_model`.`domain` HAVING NOT (COUNT(DISTINCT `some_model`.`username`) <= 1 ) ORDER BY NULL', only_multi_user_domains)

google_or_microsoft_domains = google_or_microsoft.values_list('domain', flat=True)
assert_query_is( 'SELECT `some_model`.`domain` FROM `some_model` WHERE (`some_model`.`domain` = google.com  OR `some_model`.`domain` = microsoft.com )' , google_or_microsoft_domains)

# Thanks, Basti, it works with Q!
with_q = SomeModel.objects.values_list('domain').annotate(cnt=models.Count('username', distinct=True)).filter(models.Q(cnt__gt=1)|models.Q(domain='microsoft.com')).values_list('domain', flat=True)
assert_query_is('SELECT `some_model`.`domain` FROM `some_model` GROUP BY `some_model`.`domain`, `some_model`.`domain` HAVING (COUNT(DISTINCT `some_model`.`username`) > 1  OR `some_model`.`domain` = microsoft.com ) ORDER BY NULL' , with_q)

#### HERE START THE BUGS - 1.3 at least ####


to_sql = lambda qs: str(qs.query)

google_or_microsoft_or_multiuser_domains = google_or_microsoft_domains|only_multi_user_domains
assert 'SELECT `some_model`.`domain` FROM `some_model` WHERE (`some_model`.`domain` = google.com  OR `some_model`.`domain` = microsoft.com )' != to_sql(google_or_microsoft_or_multiuser_domains), 'should not have dropped the having filter criteria, but did %r' % to_sql(google_or_microsoft_or_multiuser_domains)

multiuser_or_google_or_microsoft = only_multi_user_domains|google_or_microsoft_domains


assert 'SELECT `some_model`.`domain` FROM `some_model` WHERE (`some_model`.`domain` = google.com  OR `some_model`.`domain` = microsoft.com ) GROUP BY `some_model`.`domain`, `some_model`.`domain` HAVING NOT (COUNT(DISTINCT `some_model`.`username`) <= 1 ) ORDER BY NULL' != to_sql(multiuser_or_google_or_microsoft), 'this should be a union query to respect the ORing applied normally, but got an effective intersection (AND): %s' % to_sql(multiuser_or_google_or_microsoft)

