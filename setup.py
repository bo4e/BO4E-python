import sys

from setuptools import setup

min_version = (3, 8)

if sys.version_info < min_version:
    error = f"""
bo4e needs Python {min_version} or above.
You are using Python {sys.version_info}
""".format(
        ".".join(str(n) for n in min_version),
        ".".join(str(n) for n in sys.version_info[:3]),
    )
    sys.exit(error)

setup(name="bo4e", use_scm_version=True)
