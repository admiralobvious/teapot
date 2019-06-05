from setuptools import setup

setup(
    name="teapot",
    version="0.0.1",
    description="",
    url="https://github.com/admiralobvious/teapot",
    author="Alexandre Ferland",
    author_email="aferlandqc@gmail.com",
    license="MIT",
    packages=["teapot"],
    zip_safe=False,
    install_requires=[
    ],
    setup_requires=["pytest-runner>=5.1"],
    tests_require=["pytest>=4.5"],
    platforms="any",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.7",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ]
)
