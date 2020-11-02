import venv
import os
from sys import platform

# Create virtual environment for Python
env_builder = venv.EnvBuilder(
	system_site_packages=False, # venv seems still to look for global packages in case of failure
	clear=True,
	symlinks=False,
	upgrade=False,
	with_pip=True,
	prompt=None)
env_builder.create('venv')
if platform == "linux" or platform == "linux2":
	pass # TODO
elif platform == "darwin":
	os.system('source venv/bin/activate & pip3 install -r requirements.txt')
elif platform == "win32":
	os.system('cd venv/Scripts & activate.bat & pip install -r ../../requirements.txt')