from distutils.core import setup

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
        'Development Status :: 0.1 - Alpha',
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
        'requests=>2.0'
        ],
    tests_require=[
        'httpretty>=0.8.0',
        ],
)