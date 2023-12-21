import os
import sys
import getpass


def main():
    username: str = getpass.getuser()
    default_install_path: str = f"C:\\Users\\{username}\\Documents"

    if os.path.exists(default_install_path):
        os.mkdir(f"{default_install_path}\\Auto_Extraction")
    else:
        print("error")


main()
