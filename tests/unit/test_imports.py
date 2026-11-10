import subprocess
import sys


def test_all_package_modules_import_without_optional_frameworks():
    # A fresh interpreter prevents the test runner's imports masking dependencies.
    code = """
import importlib
import pkgutil
import sys
import pid_parser
for module in pkgutil.walk_packages(pid_parser.__path__, pid_parser.__name__ + "."):
    importlib.import_module(module.name)
heavy = {"torch", "ultralytics", "paddleocr", "paddle", "networkx", "shapely",
         "streamlit", "numpy", "cv2"}
assert not heavy.intersection(sys.modules), heavy.intersection(sys.modules)
"""
    subprocess.run([sys.executable, "-c", code], check=True)
