from fabric.api import *
from fabric.contrib.files import append
from fabric.decorators import task

@task
def install_anaconda():
    sudo('curl https://repo.continuum.io/archive/Anaconda3-4.3.1-Linux-x86_64.sh -O')
    sudo('yum install bzip2 -y')
    sudo('sh ./Anaconda3-4.3.1-Linux-x86_64.sh')

@task
def  setup_anaconda():
    append('~/.bash_profile',
           'PATH=/home/tomohito/anaconda3/bin:$PATH',
           use_sudo=True
    )
