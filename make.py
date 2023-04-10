from daemontool import NuitkaMake, CURRENTWORKDIR as CWD, SEP
import platform
import os

exe = "popups"
if platform.system() == "Windows":
    os.system(f"del /f /s /q {exe}.exe")
else:
    os.system(f"rm {CWD}{SEP}{exe}")

nm = NuitkaMake("popups.py")
nm.ADD_ARG('onefile')
nm.ADD_ARG('standalone')
nm.ADD_ARG('remove-output')
nm.ADD_ARG('follow-imports')
if platform.system() == "Windows":
    nm.ADD_ARG('disable-console')
nm.ADD_ARG(f'output-filename="popups"')
nm.ADD_ARG('enable-plugin=tk-inter')
nm.ADD_ARG(f'output-dir="{CWD}"')
nm.MAKE()