import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="nif-rest-api-client",
    version="0.0.7",
    author="Einar Huseby",
    author_email="einar.huseby@gmail.com",
    description="Tools to programmatically interact with NIF's REST Api",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/luftsport/nif-rest-api-client",
    packages=setuptools.find_packages(),
    install_requires=['requests_oauthlib', 'requests', 'python-dateutil', 'oauthlib', 'retry', 'inflection'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
