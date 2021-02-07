from setuptools import setup
setup(
    name = 'goaltracker',
    version = '0.1.0',
    packages = ['goaltracker'],
    entry_points = {
        'console_scripts': [
            'goaltracker = goaltracker.__main__:main'
        ]
    })
