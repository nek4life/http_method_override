import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.txt')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

requires = [
    'webob',
    ]

setup(name="http_method_override",
      version='0.0',
      description='http_method_override',
      long_description=README + '\n\n' +  CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Middleware",
        ],
      author='',
      author_email='',
      url='',
      keywords='web wsgi webob',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      test_suite='mo',
      install_requires = requires,
      entry_points = """\
      [paste.filter_app_factory]
      http_method_override = mo:make_method_override_middleware
      """
      )

