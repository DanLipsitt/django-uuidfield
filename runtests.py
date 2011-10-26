#!/usr/bin/env python
import sys
from os.path import dirname, abspath

from django.conf import settings

if not settings.configured:
    settings.configure(
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.postgresql_psycopg2',
                'NAME': 'uuidfield_test',
            },
            'sqlite': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': ':memory:',
            }
        },
        INSTALLED_APPS=[
            'django_nose',
            'django.contrib.contenttypes',
            'uuidfield.uuidfield_tests',
        ],
        ROOT_URLCONF='',
        DEBUG=False,
        TEST_RUNNER = 'django_nose.NoseTestSuiteRunner',
    )

try:
    from django_nose import NoseTestSuiteRunner as DjangoTestSuiteRunner
except ImportError:
    from django.test.simple import DjangoTestSuiteRunner

def runtests(*test_args):
    if not test_args:
        test_args = ['uuidfield.uuidfield_tests']
    parent = dirname(abspath(__file__))
    sys.path.insert(0, parent)
    failures = DjangoTestSuiteRunner(verbosity=1, interactive='--no-input' not in sys.argv).run_tests(test_args)
    sys.exit(failures)

if __name__ == '__main__':
    runtests()
