from setuptools import setup, find_packages

setup(
    name="crm",
    version="1.0.0",
    description="Sistema CRM de consola con SQLite",
    author="Agustin Fiegler",
    author_email="agustinfiegler@gmail.com",
    packages=find_packages(),
    install_requires=[],
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'crm-console=crm.main:main',
        ],
    },
    python_requires='>=3.8',
)
