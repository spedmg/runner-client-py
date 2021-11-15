import setuptools

setuptools.setup(
    name='runner_client',
    version='1.2.0',
    author='Sony Pictures - Digital Media Group',
    author_email='runner_help@spe.sony.com',
    description='API client for Sony Pictures Runner / Compass API',
    long_description='file: README.md',
    long_description_content_type='text/markdown',
    url='https://github.com/spedmg/runner-client-py',
    project_urls = {
        'Bug Tracker': 'https://github.com/spedmg/runner-client-py/issues'
        },
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent'
        ],
    packages=setuptools.find_packages(include=['runner_client', 'runner_client.*']),
    install_requires=['attrs', 'requests']
    )
