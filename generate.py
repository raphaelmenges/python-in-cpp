import venv
import os

# Create virtual environment for Python
env_builder = venv.EnvBuilder(
	system_site_packages=False, # venv seems still to look for global packages in case of failure
	clear=True,
	symlinks=False,
	upgrade=False,
	with_pip=True,
	prompt=None)
env_builder.create('venv')
os.system('cd venv/Scripts & activate.bat & pip install -r ../../requirements.txt')