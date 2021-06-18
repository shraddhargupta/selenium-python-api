from setuptools import setup, find_packages

setup(name="allapitest", version='1.0', description=" API TESTING FRAMEWORK",
      packages=find_packages(),
      author="Shraddha Gupta",
      zip_safe=False,
               install_requires=[
            "pytest",
            "pytest-html",
            "requests",
            "requests-oauthlib",
      ]
      )
