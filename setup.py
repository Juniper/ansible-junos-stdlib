#!/usr/bin/env python
from setuptools import setup
from version import VERSION

setup(
    name="ansible-junos-stdlib",
    version=VERSION,
    author="Jeremy Schulman, Nitin Kumar, Rick Sherman, Stacy Smith",
    author_email="jnpr-community-netdev@juniper.net",
    description=("Ansible Network build automation of Junos devices."),
    license="Apache 2.0",
    keywords="Ansible Junos NETCONF networking automation",
    url="http://www.github.com/Juniper/ansible-junos-stdlib",
    packages=['library'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Telecommunications Industry',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Networking',
        'Topic :: Text Processing :: Markup :: XML'
    ],
)
