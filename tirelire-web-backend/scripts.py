import os
import subprocess

os.environ["CONFIG_PATH"] = "./tests/test_config.yaml"

def test():
    subprocess.run(
        ["python", "-m", "coverage", "run", "-m", "unittest", "discover"]
    )

def report():
    subprocess.run(
        ["python", "-m", "coverage", "report", "-m"]
    )

def audit():
    subprocess.run(
        ["pylama", "--ignore", "E24,W504", "--skip", "*__init__.py", "--report", ".audit", "app"]
    )
