from setuptools import setup
import os

version_path = os.path.join(os.path.abspath(os.path.dirname(__file__)),
                            "freecad", "hacker_space_workbench", "version.py")
with open(version_path) as fp:
    exec(fp.read())

setup(name='freecad.hacker_space_workbench',
      version=str(__version__),
      packages=['freecad',
                'freecad.hacker_space_workbench'],
      maintainer="Tpj-root",
      maintainer_email="trichyhackerspace@gmail.com",
      url="https://github.com/Tpj-root/HackerspaceWorkbench",
      description="External workbenches in FreeCAD add extra tools for specific tasks.",
      install_requires=['numpy',],
      include_package_data=True)
