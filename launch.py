import argparse
import importlib
import pathlib
import sys
import os

path = pathlib.Path(__file__).parent


def install_deps():
    for dep in ("pysect", "nicegui", "pywebview"):
        try:
            importlib.import_module(dep)
        except ModuleNotFoundError:
            print(f"Installing {dep}")
            os.system(f"{sys.executable} -m pip install {dep}")


def run():
    print("Launching pysect!")
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--cui", action="store_true")
    parser.add_argument("-s", "--standalone", action="store_true")

    args = parser.parse_args()
    if args.cui:
        os.system(f"{sys.executable} {path / 'src'/ 'main.py'}")
    elif args.standalone:
        os.system(f"{sys.executable} {path / 'standalone.py'}")
    else:
        os.system(f"{sys.executable} {path / 'main.py'}")


def main():
    print(r"                                __ ")
    print(r"    ____  __  __________  _____/ /_")
    print(r"   / __ \/ / / / ___/ _ \/ ___/ __/")
    print(r"  / /_/ / /_/ (__  )  __/ /__/ /_  ")
    print(r" / .___/\__, /____/\___/\___/\__/  ")
    print(r"/_/    /____/     (c) 2024 Anonoei ")
    install_deps()
    run()


if __name__ == "__main__":
    main()
