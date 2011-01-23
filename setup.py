from setuptools import setup, find_packages
import sys, os

version = '1.0'
shortdesc = 'bda.bfg.ugm'
longdesc = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

setup(name='bda.bfg.ugm',
      version=version,
      description=shortdesc,
      long_description=longdesc,
      classifiers=[
            'Development Status :: 3 - Alpha',
            'Environment :: Web Environment',
            'Operating System :: OS Independent',
            'Programming Language :: Python', 
            'Topic :: Internet :: WWW/HTTP :: Dynamic Content',        
      ],
      keywords='',
      author='BlueDynamics Alliance',
      author_email='dev@bluedynamics.com',
      url=u'http://github.com/bluedynamics/bda.bfg.ugm',
      license='GNU General Public Licence',
      packages=find_packages('src'),
      package_dir = {'': 'src'},
      namespace_packages=['bda', 'bda.bfg'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'bda.bfg.app',
          'node.ext.ldap',
          'yafowil.widget.datetime',
          'yafowil.widget.richtext',
          'yafowil.widget.dict',
          'yafowil.widget.autocomplete',
          'yafowil.widget.dynatree',
      ],
      extras_require = dict(
          test=[
                'interlude',
          ]
      ),
      tests_require=[
          'interlude',
      ],
      test_suite = "bda.bfg.ugm.tests.test_suite",
      entry_points = """\
      [paste.app_factory]
      app = bda.bfg.ugm.run:app
      """        
      )
