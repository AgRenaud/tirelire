import os
import subprocess


def test():
    subprocess.run(
        ["python", "-m", "coverage", "run", "-m", "unittest", "discover"]
    )

def report():
    subprocess.run(
        ["python", "-m", "coverage", "report", "-m"]
    )

def format():
    subprocess.run(
        ["black", "app"]
    )
