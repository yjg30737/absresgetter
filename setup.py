import codecs
import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

setup(
    name='absresgetter',
    version='0.0.11',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    description='Get absolute resource path of exterior package',
    url='https://github.com/yjg30737/absresgetter.git',
    long_description_content_type='text/markdown',
    long_description=long_description
)