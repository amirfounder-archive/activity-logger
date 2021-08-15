from setuptools import setup

setup(
  name="activity-logger",
  version="0.0.1",
  description="Logs activity to a file",
  py_modules=[
    "main",
    "utils"
  ],
  package_dir={
    "":"src"
  }
)