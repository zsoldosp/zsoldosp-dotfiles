I wish https://docs.djangoproject.com/en/1.3/topics/db/aggregation/ included https://docs.djangoproject.com/en/1.3/ref/models/querysets/#id8
 distinct=True
qs = MyModel.objects.values_list('natural_id').annotate(cnt=Count('some_other_dimension', distinct=True)).filter(cnt__gte=2)

