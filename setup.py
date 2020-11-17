from setuptools import find_packages, setup
import os.path
import subprocess
import sys
from setuptools.command.install import install as _install
from distutils.sysconfig import get_python_lib

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
    package_data={  # Optional
        'research_jupyter_templates': ['*.ipynb'],
    },
)