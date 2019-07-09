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
        "certifi>=2019.3.9",
        "urllib3>=1.25.3",
    ],
    setup_requires=["pytest-runner>=5.1"],
    tests_require=[
        "pytest>=5.0.1",
        "python-rapidjson>=0.7.2",
        "urllib3-mock>=0.3.3"
    ],
    platforms="any",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.7",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ]
)

