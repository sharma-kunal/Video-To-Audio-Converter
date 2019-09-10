#!/usr/bin/python3

import os
import subprocess
import moviepy.editor as mp

def sendmessage(message):
    	subprocess.Popen(['notify-send', message])
    	return

paths = os.environ['NAUTILUS_SCRIPT_SELECTED_FILE_PATHS'].splitlines()
for p in paths:
    	sendmessage(p)

try:
	#name = str(p.split('/')[-1]).split('.')[-1]
	#sendmessage(name)
	video = mp.VideoFileClip(p)
	video.audio.write_audiofile("Converted_Audio.mp3")
	sendmessage("Done")
except Exception as e:
        sendmessage("An Error Occured")

