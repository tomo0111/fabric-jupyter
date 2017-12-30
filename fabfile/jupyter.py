from cuisine import file_upload, sudo
from fabric.decorators import task

@task
def setup_jupyter():
    file_upload('/opt/.jupyter/jupyter_notebook_config.py', 'files/jupyter_notebook_config.py', sudo=True)

@task
def setup_system():
    file_upload('/etc/systemd/system/notebook.service', 'files/notebook.service', sudo=True)

@task
def start_service():
    sudo('systemctl daemon-reload')
    sudo('systemctl start notebook')
    sudo('systemctl enable notebook')