import warnings
import os
import platform

try:
    from distribute_setup import use_setuptools
    use_setuptools()
except:
    warnings.warn(
    "Failed to import distribute_setup, continuing without distribute.", 
    Warning)

from setuptools import setup, find_packages

readme_text = file(os.path.join(os.path.dirname(__file__), 'README.md'), 'rb').read()

with open('marinemap_requirements.txt') as f:
    lines = f.read().splitlines()

from lingcod.common.release import RELEASE

if platform.system is 'Windows':
    deps = [line for line in lines if line.startswith('#') is False and len(line) > 0 and line.startswith('GDA') is False]
else:
    deps = [line for line in lines if line.startswith('#') is False and len(line) > 0]
    
setup_args = dict(
    name                = 'marinemap',
    version             = RELEASE,
    #requires_python     = '>=2.5,<3',
    #requires_external  = 
    install_requires    = deps,
    description         = 'A framework for building decisison support tools supporting marine spatial planning',
    author              = 'MarineMap Consortium',
    author_email        = 'mcclintock@msi.ucsb.edu',
    maintainer          = 'MarineMap Consortium',
    maintainer_email    = 'mcclintock@msi.ucsb.edu',
    url                 = 'http://code.google.com/p/marinemap',
    license             = 'New BSD License',
    keywords            = 'kml marine decisionsupport science gis',
    long_description    = readme_text,
    packages            = ['lingcod.%s' % x for x in find_packages(os.path.join(os.path.dirname(__file__), 'lingcod'))],
    #scripts            = 
    #test_suite         = 
    classifiers         = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Scientific/Engineering :: GIS',
        'Framework :: Django',
        'Environment :: Web Development'
        ],
    )

setup(**setup_args)
