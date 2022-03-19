from setuptools import setup, find_packages


def parse_requirements(filename):
    """ load requirements from a pip requirements file """
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if line and not line.startswith("#")]

# parse_requirements() returns generator of pip.req.InstallRequirement objects
install_reqs = parse_requirements("requirements.txt")

setup(
    name='DockingPP',
    version="0.0.1",
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    install_requires=install_reqs
)
