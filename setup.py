from setuptools import setup, find_packages

setup(
    name="foo_parameterization",
    version="0.1.0",
    description="A package to calculate the Foo et al. parameterization of a sphere's volume.",
    author="Adil Asad",
    author_email="adilasad1@hotmail.com",
    packages=find_packages(),
    install_requires=[
        # Add dependencies here
    ],
    entry_points={
        'console_scripts': [
            'foo_volume=foo_parameterization.cli:main',
        ],
    },
)
