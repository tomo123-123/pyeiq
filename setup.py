import os
import pathlib
import shutil
from setuptools import setup, find_packages

setup(name="eiq",
version="1.0",
description="eIQ package provides classes and scripts to manage the eIQ Samples Apps.",
url="",
author="Diego Dorta <diego.dorta@nxp.com>, Alifer Moraes <alifer.moraes@nxp.com>",
author_email="diego.dorta@nxp.com",
license="BDS-3-Clause",
packages=find_packages(),
zip_safe=False)

init = "__init__.py"
demos_dir = os.path.join(os.getcwd(), "eiq", "demos")
install_dir = os.path.join("/opt", "eiq", "demos")

if not os.path.exists(install_dir):
    try:
        pathlib.Path(install_dir).mkdir(parents=True, exist_ok=True)
    except OSError:
        sys.exit("os.mkdir() function has failed: %s" % install_dir)

for file in os.listdir(demos_dir):
    if file != init:
        file = os.path.join(demos_dir, file)
        shutil.copy(file, install_dir)