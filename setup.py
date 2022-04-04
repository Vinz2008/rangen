import setuptools

with open("README.md","r") as fh:
	long_description = fh.read()

setuptools.setup(
    name='rangen',  
    version='0.1',
    author="Vincent Bidard de la Noë",
    author_email="vincentbidarddelanoe@gmail.com",
    description="Rangen is a random string generator.",
    long_description=long_description,
    url="https://github.com/Vinz2008/rangen",
    scripts=["rangen"],
    classifiers=[
    ],
