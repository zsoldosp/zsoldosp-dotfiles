class AdminLookupProblemReproTestCase(TestCase):
    class models:
        class MyModel(models.Model):
            pass # implicit pk

    class admin:
        class MyModelAdmin(admin.ModelAdmin):
            allowed_lookups = ['pk__in']

    def test_cannot_lookup_with_trailing_L_indicating_long(self):
        self.register()
        self.client.login_as_admin()
        self.client.get('/reprto/mymodel/?pk__in=[1L]')
        # raises exception :(
        # TODO: repro against 1.5/1.6 and file report if needed
