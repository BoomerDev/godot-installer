#!/usr/bin/env python3

import urllib.request
import os
import sys

import zipfile
import subprocess

print("Godot 4.0 versions can be found at 'https://download.tuxfamily.org/godotengine/4.0' (excluding pre-alpha).")

version = input("Please specify the version of Godot Engine 4.0 that you would like to download: ")
path = "https://download.tuxfamily.org/godotengine/4.0/%s/Godot_v4.0-%s_linux.x86_64.zip" % (version, version)

urllib.request.urlretrieve(path, "/tmp/GodotEnginePackage_000.zip")

if os.path.exists("/tmp/GodotEnginePackage_000.zip"):
    print("Successfully downloaded Godot Engine package")

with zipfile.ZipFile("/tmp/GodotEnginePackage_000.zip", 'r') as zrf:
    zrf.extractall("/tmp/GodotEnginePackage_000_tmpdir")
    subprocess.run(["rm", "/tmp/GodotEnginePackage_000.zip"])

subprocess.run(["cp", "/tmp/GodotEnginePackage_000_tmpdir/Godot_v4.0-%s_linux.x86_64" % version, "/usr/bin/godot4_%s" % version])
subprocess.run(["chmod", "+x", "/usr/bin/godot4_%s" % version])

print("Created command 'godot4_%s'. You can now run this in the terminal." % version)

yn = input("Would you like install overwrite any previous installation of the Godot engine (/usr/bin/godot4)? ")

if yn[0] in ('Y', 'y'):
    subprocess.run(["cp", "/usr/bin/godot4_%s" % version, "/usr/bin/godot4"])
    subprocess.run(["chmod", "+x", "/usr/bin/godot4"])

    print("Created command 'godot4'. You can now run this in the terminal.")

print("Cleaning up...")
subprocess.run(["rm", "-rf", "/tmp/GodotEnginePackage_000_tmpdir/"])
print("Done!")
