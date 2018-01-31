from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='thecypher',  
    version='1.2.2', 
    description='Get music lyrics',
    long_description=long_description,  
    url='https://github.com/tmthyjames/thecypher', 
    author='Timothy James Dobbins',  
    author_email='tmthyjames@gmail.com', 
    classifiers=[  
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='thecypher setuptools development',  
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),  
    install_requires=['requests', 'beautifulsoup4'],  
    extras_require={  
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },
    package_data={  
        'thecypher': ['package_data.dat'],
    },
    data_files=[('my_data', ['data/data_file'])],  
    entry_points={ 
        'console_scripts': [
            'thecypher=thecypher:get_lyrics',
        ],
    },
)
