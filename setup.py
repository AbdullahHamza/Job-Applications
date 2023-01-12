from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in job_applications/__init__.py
from job_applications import __version__ as version

setup(
	name="job_applications",
	version=version,
	description="Handeling job applications",
	author="Abdullah",
	author_email="abhamza213@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
