import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name='glogger',
    version='1.0.0',
    description="A python library for logging loguru messages straight to a gelf instance, for example Sematext via HTTP",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/fino-digital/glogger",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "requests",
        "loguru"
    ]
)
