import setuptools

setuptools.setup(
    author="Allen Goodman",
    author_email="allen.goodman@icloud.com",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    extras_require={
        "dev": [
            "sphinx>=3.1.2",
            "twine==3.1.1",
        ],
        "test": ["pytest~=7.4.1"],
        "wx": ["wxPython==4.1.0"],
    },
    install_requires=[
        "boto3==1.14.23",
        "centrosome==1.2.3",
        "docutils==0.15.2",
        "fsspec==2022.2.0",
        "h5py==3.6.0",  # Consider 3.2.1 if problems happen
        "matplotlib==3.1.3",
        "numpy==1.23.1",
        "prokaryote==2.4.4",
        "psutil==5.7.0",
        "python-bioformats==4.1.0",
        "python-javabridge==4.0.4",
        "pyzmq==22.3.0",
        "Pillow==8.3.2",
        "scikit-image==0.18.3",
        "scipy==1.9.0",
        "zarr==2.10.2",
    ],
    license="BSD",
    name="cellprofiler-core",
    package_data={"cellprofiler_core": ["py.typed"]},
    packages=setuptools.find_packages(exclude=["tests"]),
    python_requires=">=3.8, <4",
    url="https://github.com/CellProfiler/core",
    version="4.2.80002",
    zip_safe=False,
)
