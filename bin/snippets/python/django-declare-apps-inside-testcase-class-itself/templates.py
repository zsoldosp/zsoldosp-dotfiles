class given_the_following_templates(object):
    """ context manager to help with library testing """

    def __init__(self, template_dict_filesystem):
        self.template_dict_filesystem = template_dict_filesystem

    def __enter__(self):
        self.dir_path = tempfile.mkdtemp(prefix='test-specific-templates')
        self.orig_template_dirs = settings.TEMPLATE_DIRS
        settings.TEMPLATE_DIRS = [ self.dir_path ]
        for template_name, data in self.template_dict_filesystem.iteritems():
            try:
                last_slash = template_name.rindex('/')
                template_dir = os.path.join((self.dir_path, template_name[:last_slash]))
                template_file = template_name[last_slash + 1:]
            except ValueError:
                template_dir = self.dir_path
                template_file = template_name
            os.mkdirs(template_dir)
            full_template_path = os.path.sep.join([template_dir, template_file])
            with open(full_template_path, 'w+') as f:
                f.write(data)

    def __exit__(self, type, value, traceback):
        shutil.rmtree(self.dir_path)
        settings.TEMPLATE_DIRS = self.orig_template_dirs 


class FooTest(TestCase):
    def test_something(self):
        with the_following_templates({
            'some/template/file.html': 'Hello {{ user.username }}!',
        }):
            self.assertRaises(TemplateDoesNotExist):
                render_to_string('no_such/template.html', {})
            self.assertEquals('Hello world!', render_to_string('some/template/file.html', dict(user=User.objects.create(username='world'))))
