from os.path import exists, join, splitext
from os import getcwd, listdir
from sys import path
import importlib
from time import sleep
import subprocess
import os
import time

directory = getcwd()

plugin_dir = join(directory, '_dat', 'MMplugins')
path.insert(0, plugin_dir) # Imports Plugins

plugin_names = ['plugin.py', 'plugin0.py', 'WTSM.py', 'plugin1.py', 'plugin2.py', 'plugin3.py']

for plugin_name in plugin_names:
    plugin_path = join(plugin_dir, plugin_name)
    if exists(plugin_path):
        plugin_module = importlib.import_module(splitext(plugin_name)[0])

wtsm_path = join(plugin_dir, 'WTSM.py')

if exists(wtsm_path):
    import WTSM
    print(f"PLUGIN: WTSM Version - {WTSM.version}")
    print(f"PLUGIN: Created By - {WTSM.developer}")
    print(" ")
    WTSM.MainApp()
    print(" ")

plugin_p = join(plugin_dir, 'plugin.py')
if exists(plugin_p):
    import plugin
    print(f"PLUGIN: Version - {plugin.version}")
    print(f"PLUGIN: Created By - {plugin.developer}")
    print(" ")
    plugin.MainApp()

plugin_p = join(plugin_dir, 'plugin0.py')
if exists(plugin_p):
    import plugin0
    print(f"PLUGIN: Version - {plugin0.version}")
    print(f"PLUGIN: Created By - {plugin0.developer}")
    print(" ")
    plugin0.MainApp()

plugin_p = join(plugin_dir, 'plugin1.py')
if exists(plugin_p):
    import plugin1
    print(f"PLUGIN: Version - {plugin1.version}")
    print(f"PLUGIN: Created By - {plugin1.developer}")
    print(" ")
    plugin1.MainApp()

plugin_p = join(plugin_dir, 'plugin2.py')
if exists(plugin_p):
    import plugin2
    print(f"PLUGIN: Version - {plugin2.version}")
    print(f"PLUGIN: Created By - {plugin2.developer}")
    print(" ")
    plugin2.MainApp()

plugin_p = join(plugin_dir, 'plugin3.py')
if exists(plugin_p):
    import plugin3
    print(f"PLUGIN: Version - {plugin3.version}")
    print(f"PLUGIN: Created By - {plugin3.developer}")
    print(" ")
    plugin3.MainApp()

directory_path = join(directory,'_dat','MMplugins')

files = listdir(directory_path)

for file in files:

    if file.endswith('.bat') or file.endswith('.vbs'):
        file_path = join(directory_path, file)
        
        if file.endswith('.bat'):
            subprocess.call(file_path, shell=True)

        elif file.endswith('.vbs'):
            subprocess.call(['cscript', '//B', file_path])

print(" ")
print("=================== ===================")
print("Finished Loading Plugins without Errors.")
print(f"Make Sure Plugins Are Located: {directory_path}.")

sleep(10)
print(" ")
input("Press 'Any' Key To Exit.")
