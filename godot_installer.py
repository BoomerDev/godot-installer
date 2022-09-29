#!/usr/bin/env python3

import urllib.request
import os
import sys

import zipfile
import subprocess

print("Godot versions can be found at 'https://download.tuxfamily.org/godotengine/' (For Godot 4.0 downloads, run 'python3 godot4_installer.py').")

version = input("Please specify the version of Godot Engine that you would like to download: ")
path = "https://download.tuxfamily.org/godotengine/%s/Godot_v%s-stable_x11.64.zip" % (version, version)

urllib.request.urlretrieve(path, "/tmp/GodotEnginePackage_000.zip")

if os.path.exists("/tmp/GodotEnginePackage_000.zip"):
    print("Successfully downloaded Godot Engine package")

with zipfile.ZipFile("/tmp/GodotEnginePackage_000.zip", 'r') as zrf:
    zrf.extractall("/tmp/GodotEnginePackage_000_tmpdir")
    subprocess.run(["rm", "/tmp/GodotEnginePackage_000.zip"])

subprocess.run(["cp", "/tmp/GodotEnginePackage_000_tmpdir/Godot_v%s-stable_x11.64" % version, "/usr/bin/godot%s" % version])
subprocess.run(["chmod", "+x", "/usr/bin/godot%s" % version])

print("Created command 'godot%s'. You can now run this in the terminal." % version)

yn = input("Would you like install overwrite any previous installation of the Godot engine (/usr/bin/godot)? ")

if yn:
    subprocess.run(["cp", "/usr/bin/godot%s" % version, "/usr/bin/godot"])
    subprocess.run(["chmod", "+x", "/usr/bin/godot"])
    
    print("Created command 'godot'. You can now run this in the terminal.")

print("Cleaning up...")
subprocess.run(["rm", "-rf", "/tmp/GodotEnginePackage_000_tmpdir/"])
print("Done!")
