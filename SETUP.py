from setuptools import setup, find_packages

setup(
    name='downloads-sorter',
    version='0.1',
    packages=find_packages(),
    description='A script to help you organise your files.',
    license='MIT license',
    install_requires=[
        'rich',
        'send2trash',
        'colorama',
    ],
    entry_points={
        'console_scripts': [
            'downloads-sorter=downloads_sorter:main',
        ],
    },
)