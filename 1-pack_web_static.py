#!/usr/bin/python3
"""
Fabric script that generates a tgz archive from the contents of the web_static
folder of the AirBnB Clone repo
"""

from datetime import datetime
from fabric.api import local
from os.path import isdir
import os


def do_pack():
    """generates a tgz archive"""
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir -p versions")
        archived_file = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(archived_file))
        file_size = os.path.getsize(archived_file)
        print('web_static packed: {} -> {}Bytes'.format(archived_file, file_size))
        return archived_file
    except:
        return None
