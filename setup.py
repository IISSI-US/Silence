import os
import re

from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

# Borrowed from urllib3 (which is in turn borrowed from SQLAlchemy)
base_path = os.path.dirname(__file__)
ver_path = os.path.join(base_path, "silence", "__init__.py")

with open(ver_path, "r") as f:
    version = re.compile(r""".*__version__ = ["'](.*?)['"]""", re.S).match(f.read()).group(1)

setup(
    name='Silence',
    version=version,
    description='An educational API+Web framework.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='http://github.com/agu-borrego/Silence',
    author='Agustín Borrego',
    author_email='borrego@us.es',
    license='MIT',
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "silence = silence.cli.manager:run_from_command_line",
        ],
    },
    install_requires=[
        'dload==0.6',
        'Flask==1.1.2',
        'PyMySQL==0.9.3',
        'sqlvalidator==0.0.3'
    ],
    python_requires='~=3.6',
    zip_safe=False
)