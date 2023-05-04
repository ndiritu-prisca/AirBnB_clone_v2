#!/usr/bin/python3
"""
    A Fabric script that generates a .tgz archive from the contents of the
    web_static folder
"""

from fabric.api import local
from datetime import datetime


def do_pack():
    """A function that generates the .tgz archive"""
    local("mkdir -p versions")
    file_name = ("versions/web_static_{}.tgz"
                 .format(datetime.strftime(datetime.utcnow(), "%Y%m%d%H%M%S")))
    tgz_file = local("tar -cvzf {} web_static"
                     .format(file_name))

    if tgz_file.failed:
        return None
    return file_name
