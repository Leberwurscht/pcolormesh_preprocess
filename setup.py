import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pcolormesh_preprocess",
    version="0.0.1",
    author="Leberwurscht",
    author_email="leberwurscht@hoegners.de",
    description="preprocess data passed to pcolormesh so that axes are aligned to the centers of the corresponding rectangles, not their borders",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/leberwurscht/pcolormesh_preprocess",
    packages=setuptools.find_packages(),
    install_requires=[
        'numpy'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3'
)
