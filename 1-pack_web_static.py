#!/usr/bin/python3
"""This will generate a .tgz archive from the web_static folder."""

from datetime import datetime
from fabric.api import local
from os import path


def do_pack():
    """Create and return an archive of web_static."""
    try:
        if not path.exists("versions"):
            local("mkdir -p versions")

        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        archive_path = "versions/web_static_{}.tgz".format(timestamp)

        print("Packing web_static to {}".format(archive_path))

        result = local(
            "tar -cvzf {} web_static".format(archive_path),
            capture=False
        )

        if result.succeeded:
            print(
                "web_static packed: {} -> {}Bytes".format(
                    archive_path,
                    path.getsize(archive_path)
                )
            )
            return archive_path

        return None

    except Exception:
        return None
