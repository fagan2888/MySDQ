import os
from setuptools import setup, find_packages
import subprocess

__author__ = 'Josue Kouka'
__username__ = 'josuebrunel'
__email__ = 'josuebrunel@gmail.com'
name = 'mysdq'

version_py = os.path.join(os.path.dirname(__file__), 'version.py')

try:
    version_git = subprocess.check_output(["git", "describe"]).rstrip()
except Exception:
    with open(version_py, 'r') as fh:
        version_git = open(version_py).read().strip().split('=')[-1].replace('"', '')

version_msg = "# Do not edit this file, pipeline versioning is governed by git tags"

with open(version_py, 'w') as fh:
    fh.write(version_msg + os.linesep + "__version__=" + version_git)


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


url = "https://github.com/%s/%s/" % (__username__, name)
download_url = url + 'archive/{version}.tar.gz'.format(version=version_git)
requirements = read('requirements.txt').splitlines() if os.path.isfile('requirements.txt') else []

setup(
    name=name,
    version=version_git,
    description="",
    long_description=read("README.rst"),
    author=__author__,
    author_email=__email__,
    url=url,
    download_url=download_url,
    keywords=[],
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Development Status :: 5 - Production/Stable',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License'
    ],
    platforms=['Any'],
    license='MIT',
    install_requires=requirements
)
