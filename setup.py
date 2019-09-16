from setuptools import setup, find_packages

setup(
    name='marshmallow_gis',
    version='0.1',
    packages=['marshmallow_gis'],
    include_package_data=True,
    install_requires=[
        'marshmallow<3.0',
        'shapely'
    ]
)
