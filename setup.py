from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='plonetheme.emgame2012',
      version=version,
      description="EM-Game 2012 theme for Plone",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='',
      author='Thomas Buchberger',
      author_email='t.buchberger@4teamwork.ch',
      url='https://github.com/4teamwork.ch/plonetheme.emgame2012',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['plonetheme'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'plone.app.theming',
      ],
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
