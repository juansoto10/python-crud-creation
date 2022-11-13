from setuptools import setup


setup(
    name='vcau',
    version='0.1',
    py_modules=['vcau'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        vcau=vcau:cli
    ''',
)
