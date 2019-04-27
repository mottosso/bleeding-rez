import os
import subprocess

pypirc = """\
[distutils]
index-servers = pypi
[pypi]
repository=https://pypi.python.org/pypi
username={PYPI_LOGIN}
password={PYPI_PASSWORD}
""".format(**os.environ)


def main():
    print("Deploying to PyPI..")

    with open(os.path.expanduser("~/.pypirc")) as f:
        f.write(pypirc)

    subprocess.check_call([
        "python", "-m", "twine", "upload", "dist/*"
    ])


if os.getenv("APPVEYOR_REPO_TAG") == "true":
    main()
else:
    print("Deployment skipped, not a tag")