
import setuptools
setuptools.setup(
   name='TagClassifer',
   version='0.1.0',
   author='tczhong',
   author_email='me@tczhong',
   packages= setuptools.find_packages(),
   url='http://pypi.python.org/pypi/PackageName/',
   license='LICENSE.txt',
   description='Filter file name with sub string',
   long_description=open('README.md').read(),
   install_requires=[
       "ruamel-yaml"
   ],
   python_requires='>=3.7',
)