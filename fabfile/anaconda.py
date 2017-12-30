from fabric.api import *
from fabric.contrib.files import append
from fabric.decorators import task

@task
def install_wget():
    sudo('yum install -y wget')

@task
def install_anaconda():
    sudo('mkdir /opt/jupyter')
    sudo('wget https://repo.continuum.io/archive/Anaconda3-4.3.1-Linux-x86_64.sh -P /opt')
    sudo('yum install -y bzip2')
    sudo('sh /opt/jupyter/Anaconda3-4.3.1-Linux-x86_64.sh')

@task
def  setup_anaconda():
    append('~/.bash_profile',
           'PATH=/opt/jupyter/anaconda3/bin:$PATH',
           use_sudo=True
    )
