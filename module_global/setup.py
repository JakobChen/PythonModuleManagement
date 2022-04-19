from setuptools import setup, find_packages

setup(name="module_global",
      version="0.1.0",
      description="my customized functions",
      author="Jacob Chen",
      packages=find_packages("mypackage"),
      package_dir={"": "mypackage"},
      author_email="jacob.chen@gmx.de",
      install_requires=["jupyter",
                        "numpy",
                        "pytest==5.2.2",
                        "pytest-mpl==0.10",
                        "pytest-mock==1.11.2",
                        "scipy",
                        ],
      )