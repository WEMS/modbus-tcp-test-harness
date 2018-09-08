from setuptools import setup

setup(name='modbus-values',
      version='1.0.0',
      description='',
      url='',
      author='Ben Cromwell',
      author_email='placeholder@example.com',
      license='MIT',
      packages=['modbusvalues'],
      install_requires=[
          'pymodbus',
      ],
      zip_safe=False,
      test_suite='nose.collector',
      tests_require=['nose'],
      entry_points={
          'console_scripts': [
              'modbusvalues = modbusvalues.command_line:main'
          ],
      }
)
