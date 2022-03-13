import setuptools

with open("README.md") as file:
    read_me_description = file.read()

setuptools.setup(
    name="oneclick_client",
    version="1.0.2",
    author="sprootik",
    author_email="sprootik89@gmail.com",
    description="Simple library to use Spectrum OneClick API.",
    long_description=read_me_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sprootik/oneclick_client.git",
    packages=['oneclick_client'],
    install_requires=['requests',  'bs4', 'requests-auth'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        "Programming Language :: Python :: 3",
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9',
)
