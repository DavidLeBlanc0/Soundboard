# FILE:     fileFunctions.py
# AUTHOR:   David LeBlanc 143807L@acadiau.ca
# DATE:     2019/11/17
# VERSION:  1.1
# PURPOSE:  This program defines functions for use in managing the files needed
# for the Chadatonic.

import sys
import tkinter as tk
import json
from tkinter import filedialog
import os
from shutil import copyfile
from pathlib import Path

# Opens a file selection prompt and returns the selected path
def file_prompt():
    root = tk.Tk()
    root.withdraw()
    filePath = filedialog.askopenfilename()

    return filePath

# Creates the directories for configurations and sounds, if they don't already
# exist
def create_directories():
    if not os.path.exists("configs"):
        os.mkdir("configs")
    if not os.path.exists("sounds"):
        os.mkdir("sounds")


# Imports a selected sound into the sounds folder so it is easy to find
# Returns -1 on error, 0 on success
def import_sound(soundPath):
    ext = str(os.path.splitext(soundPath)[1])
    path = str(Path(soundPath).stem)

    # Return error if unusable format
    if ext != ".wav":
        return -1

    # Return error if directories do not exist
    if not os.path.exists("sounds"):
        return -1

    copyfile(soundPath, "sounds/" + path + ext)

    return 0

# Saves a sound config with given settings in configData
# configData[0] = sound name
# configData[1] = volume
def save_sound_config(configData):
    data = {}
    data["content"] = []
    data["content"].append({
        "soundname": configData[0],
        "volume": configData[1]
    })

    with open("configs/" + configData[0] + ".json", 'w') as outfile:
        json.dump(data, outfile)

# Returns the config data for a specified sound
# returnData[0] = sound name
# returnData[1] = volume
def load_sound_config(soundName):
    returnData = [None]*2

    # Open JSON
    with open("configs/" + soundName + ".json") as config_file:
        data = json.load(config_file)
        # Loop through file to find the correct sound
        for sound in data['content']:
            if sound["soundname"] == soundName:
                returnData[0] = sound["soundname"]
                returnData[1] = sound["volume"]

    return returnData