#!/usr/bin/python3
""" Fabric script that distributes an archive to your web servers,
using the function do_deploy """
from fabric.api import env, put, run
import os

env.hosts = ['54.89.134.41', '35.174.213.64']
env.user = 'ubuntu'


def do_deploy(archive_path):
    """ Distributes an archive to your web servers """
    if not os.path.exists(archive_path):
        return False

    try:
        put(archive_path, '/tmp/')
        filename = os.path.basename(archive_path)
        foldername = '/data/web_static/releases/' + \
            os.path.splitext(filename)[0]
        run('mkdir -p {}'.format(foldername))
        run('tar -xzf /tmp/{} -C {}'.format(filename, foldername))
        run('rm /tmp/{}'.format(filename))
        run('rm -rf /data/web_static/current')
        run('ln -s {} /data/web_static/current'.format(foldername))

        return True
    except Exception as e:
        return False
