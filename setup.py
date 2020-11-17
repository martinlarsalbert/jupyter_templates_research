from setuptools import find_packages, setup
import codecs
import os.path
import subprocess
import sys
from setuptools.command.install import install as _install
from distutils.sysconfig import get_python_lib
from research_jupyter_templates import _version

DISTNAME = 'research_jupyter_templates'
DESCRIPTION = "I will here be experimenting with jupyter notebook templates, with a good structure that enforces good documentation and that can be used over and over again."
with codecs.open('README.md', encoding='utf-8-sig') as f:
    LONG_DESCRIPTION = f.read()
MAINTAINER = 'Martin Alexandersson'
MAINTAINER_EMAIL = 'maa@sspa.se'
URL = 'https://github.com/martinlarsalbert/research_jupyter_templates'
LICENSE = 'MIT'
DOWNLOAD_URL = 'https://github.com/martinlarsalbert/research_jupyter_templates'
VERSION = _version.__version__
INSTALL_REQUIRES = ['versioneer','jupyterlab','jupyterlab_templates']
CLASSIFIERS = ['Intended Audience :: Science/Research',
               'Intended Audience :: Developers',
               'License :: OSI Approved',
               'Programming Language :: Python',
               'Topic :: Software Development',
               'Topic :: Scientific/Engineering',
               'Operating System :: Microsoft :: Windows',
               'Operating System :: POSIX',
               'Operating System :: Unix',
               'Operating System :: MacOS',
               'Programming Language :: Python :: 2.7',
               'Programming Language :: Python :: 3.5',
               'Programming Language :: Python :: 3.6',
               'Programming Language :: Python :: 3.7']
EXTRAS_REQUIRE = {}


def copy_templates():
    import research_jupyter_templates
    import os.path
    import shutil
    import glob
    
    
    for file in glob.glob(os.path.join(research_jupyter_templates.path,'*.ipynb')):
        
        site_packages_path = get_python_lib()
    
        dest_dir = os.path.join(site_packages_path,'jupyterlab_templates','templates','jupyterlab_templates')
    
        print('Copy %s to %s' %(file,dest_dir))
    
        shutil.copy(file, dest_dir)


class Install(_install):
    def run(self):
        _install.run(self)
        
        
        process = subprocess.run(['jupyter', 'labextension', 'install', 'jupyterlab_templates'], 
                         stdout=subprocess.PIPE, 
                         universal_newlines=True)
                         
        process = subprocess.run([ 'jupyter', 'serverextension', 'enable', 'jupyterlab_templates'], 
                         stdout=subprocess.PIPE, 
                         universal_newlines=True)


        copy_templates()

setup(
    name=DISTNAME,
    maintainer=MAINTAINER,
    maintainer_email=MAINTAINER_EMAIL,
    description=DESCRIPTION,
    license=LICENSE,
    url=URL,
    version=VERSION,
    download_url=DOWNLOAD_URL,
    long_description=LONG_DESCRIPTION,
    zip_safe=False,  # the package can run out of an .egg file
    classifiers=CLASSIFIERS,
    packages=find_packages(),
    install_requires=INSTALL_REQUIRES,
    extras_require=EXTRAS_REQUIRE,
    cmdclass={'install':Install},
    package_data={  # Optional
        'research_jupyter_templates': ['*.ipynb'],
    },
)