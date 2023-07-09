#!/usr/bin/python3
from fabric.api import local
from datetime import datetime
import os

def do_pack():
    """
    Generate a .tgz archive from the contents of the web_static folder.
    Return the archive path if generated successfully, otherwise return None.
    """
    # Create the versions directory if it doesn't exist
    if not os.path.exists("versions"):
        os.makedirs("versions")

    # Generate the timestamp for the archive name
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

    # Set the archive path
    archive_path = "versions/web_static_{}.tgz".format(timestamp)

    # Compress the web_static folder into the archive
    result = local("tar -czvf {} web_static".format(archive_path))

    if result.failed:
        return None
    else:
        return archive_path
