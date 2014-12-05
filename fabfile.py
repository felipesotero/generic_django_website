#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fabric.api import lcd, local, run, env, cd, prompt
from fabric.colors import green, red

def server():
    """This pushes to the EC2 instance defined below"""
    # The Elastic IP to your server
    env.host_string = 'yourwebsite.com'
    env.timeout = 30
    env.port = 22
    # your user on that system
    env.user = 'username_on_yourwebsite.com'

    # env.key_filename = 'ec2_key.pem'

def staging():
    # path to the directory on the server where your vhost is set up
    home = '/home/web'
    path = "/home/web/webapps"
    # name of the restart shell script: This should include services restart for gunicorn, nginx, apache or uwsgi processes.
    process = "restart.sh"

    print(red("Beginning Deploy:"))
    with cd("{path}/project_directory".format(path=path)):
        run("pwd")
        branch_name = prompt('Checkout to which branch? ')

        print(green("Pulling {branch_name} from GitHub...".format(branch_name=branch_name)))
        run("git pull origin {branch_name}".format(branch_name=branch_name))

        print(green("Installing requirements..."))
        run("source {home}/.virtualenvs/virtualenv_name/bin/activate && pip install -r requirements.txt".format(home=home))

        print(green("Collecting static files..."))
        run("source {home}/.virtualenvs/virtualenv_name/bin/activate && python manage.py collectstatic --noinput".format(home=home))

        print(green("Migrating the database..."))
        run("source {home}/.virtualenvs/virtualenv_name/bin/activate && python manage.py migrate".format(home=home))

    with cd('{path}'.format(path=path)):
        print(green("Restart the gunicorn and nginx process"))
        run("./restart.sh")

    print(red("DONE!"))