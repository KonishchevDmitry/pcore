"""pcore installation script."""

from __future__ import unicode_literals

from setuptools import find_packages, setup

if __name__ == "__main__":
    with open("README") as readme:
        setup(
            name = "pcore",
            version = "0.2.1",

            description = readme.readline().strip(),
            long_description = readme.read().strip() or None,
            url = "http://github.com/KonishchevDmitry/pcore",

            license = "MIT",
            author = "Dmitry Konishchev",
            author_email = "konishchev@gmail.com",

            classifiers = [
                "Development Status :: 4 - Beta",
                "Intended Audience :: Developers",
                "License :: OSI Approved :: MIT License",
                "Operating System :: MacOS :: MacOS X",
                "Operating System :: POSIX",
                "Operating System :: Unix",
                "Programming Language :: Python :: 2",
                "Programming Language :: Python :: 3",
                "Topic :: Software Development :: Libraries :: Python Modules",
            ],
            platforms = [ "unix", "linux", "osx" ],

            packages = find_packages(),
        )
