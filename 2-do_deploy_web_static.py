#!/usr/bin/python3
"""Deploy an archive of static html to my web servers with Fabric3"""

from fabric import api
from fabric.contrib import files
import os


api.env.hosts = ['142.44.167.235', '144.217.246.199']
api.env.user = 'ubuntu'
api.env.key_filename = '~/.ssh/holberton'


def do_deploy(archive_path):
    """Function to transfer `archive_path` to web servers.
    """     
            api.run('rm -rdf {}'.format(outpath))
            api.run('mkdir -p {}'.format(outpath))
            api.run('tar -xzf {} -C {}'.format(putpath[0], outpath))
            api.run('rm -f {}'.format(putpath[0]))
            api.run('mv -u {}/web_static/* {}'.format(outpath, outpath))
            api.run('rm -rf {}/web_static'.format(outpath))
            api.run('rm -rf /data/web_static/current')
            api.run('ln -sf {} /data/web_static/current'.format(outpath))
            print('New version deployed!')
        except:
            return False
        else:
            return True
