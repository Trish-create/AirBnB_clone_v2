#!/usr/bin/python3
"""Create and distribute an archive to web servers."""

from fabric.api import env
from os.path import exists
from imp import load_source

pack_module = load_source(
    "pack_module", "1-pack_web_static.py"
)
deploy_module = load_source(
    "deploy_module", "2-do_deploy_web_static.py"
)

do_pack = pack_module.do_pack
do_deploy = deploy_module.do_deploy

env.hosts = ['<IP web-01>', '<IP web-02>']


def deploy():
    """Create and deploy an archive to both web servers."""
    archive_path = do_pack()

    if not archive_path or not exists(archive_path):
        return False

    return do_deploy(archive_path)
