from glob import glob
import os
import pkg_resources

from .__about__ import __version__

templates = pkg_resources.resource_filename("dt_publisher", "templates")

config = {
    "add": {
        "TEST": "Value",
    },
    "defaults": {
        "MFE_APP": {
            "name": "publisher",
            "repository": "https://github.com/Dicey-tech/frontend-app-publisher",
            "port": 18400,
            "version": "master",
        }
    },
}

hooks = {}


def patches():
    all_patches = {}
    patches_dir = pkg_resources.resource_filename("dt_publisher", "patches")
    for path in glob(os.path.join(patches_dir, "*")):
        with open(path) as patch_file:
            name = os.path.basename(path)
            content = patch_file.read()
            all_patches[name] = content
    return all_patches
