from setuptools import setup, find_packages

requires = [
    'docopt',
    'keyring'
]

setup(
    name='imap-attachment-extractor',
    version='1.0',
    long_description=__doc__,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,
    entry_points={
        'console_scripts': [
            'imap_aex           = imap_aex:cli'
        ]
    },
    dependency_links=[]
)