from setuptools import find_packages, setup
import os.path
import subprocess
import sys
from setuptools.command.install import install as _install


class Install(_install):
    def run(self):
        _install.run(self)
        
        
        process = subprocess.run(['jupyter', 'labextension', 'install', 'jupyterlab_templates'], 
                         stdout=subprocess.PIPE, 
                         universal_newlines=True)
                         
        process = subprocess.run([ 'jupyter', 'serverextension', 'enable', 'jupyterlab_templates'], 
                         stdout=subprocess.PIPE, 
                         universal_newlines=True)

setup(
    name='research_jupyter_templates',
    packages=find_packages(),
    version='0.1.0',
    description="Documenting what my notebooks do is something that I'm usually pretty lazy about. I will here be experimenting with jupyter notebook templates, with a good structure that enforces good documentation and that can be used over and over again.",
    author='Martin Alexandersson',
    license='MIT',
    install_requires=['jupyterlab','jupyterlab_templates'],
    cmdclass={ 
                    'install': Install,
                    },
)