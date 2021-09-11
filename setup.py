import setuptools

setuptools.setup(
    name='rangen',  
    version='0.1',
    author="Vincent Bidard de la Noë",
    author_email="vincentbidarddelanoe@gmail.com",
    description="Rangen is a random string generator.",
    long_description="Rangen is a random string generator.",
    url="https://github.com/Vinz2008/rangen",
    packages=["rangen"],
    entry_points = {
        "console_scripts": ['rangen = rangen.rangen:main']
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
