from setuptools import setup

setup(
    name='HolyTransaction',
    version='0.1',
    packages=['holytransaction'],
    url='https://bitbucket.org/noveltylab/ht-client-python',
    license='MIT',
    author='Andrey Zamovskiy',
    author_email='andrey@noveltylab.com',
    description='Python client for HolyTransaction API',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
        ],
    install_requires=[
        'httplib2>=0.8',
        'requests>=1.1.0',
        ],
    tests_require=[
        'sure>=1.2.5',
        'httpretty>=0.8.0',
        ],
)