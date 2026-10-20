#!/usr/bin/python3
"""This is a Distribution of  an archive to web servers."""

from fabric.api import env, put, run
from os.path import exists, basename, splitext

env.hosts = ['<IP web-01>', '<IP web-02>']


def do_deploy(archive_path):
    """Deploy an archive to both web servers."""
    if not exists(archive_path):
        return False

    try:
        filename = splitext(basename(archive_path))[0]
        archive_name = basename(archive_path)
        release_path = (
            "/data/web_static/releases/{}".format(filename)
        )
        remote_archive = "/tmp/{}".format(archive_name)

        # Upload the archive to the server
        put(archive_path, "/tmp/")

        # Create the release directory
        run("mkdir -p {}".format(release_path))

        # Extract the archive
        run(
            "tar -xzf {} -C {}".format(
                remote_archive, release_path
            )
        )

        # Delete the uploaded archive
        run("rm {}".format(remote_archive))

        # Move the files out of the web_static directory
        run(
            "mv {}/web_static/* {}/".format(
                release_path, release_path
            )
        )

        # Remove the extra web_static directory
        run("rm -rf {}/web_static".format(release_path))

        # Remove the old symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run(
            "ln -s {} /data/web_static/current".format(
                release_path
            )
        )

        print("New version deployed!")
        return True

    except Exception:
        return False
