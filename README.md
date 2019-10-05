# Video to Audio Converter Script (Python3)

This is a simple Video to Audio Converter written in `python3` that can be used to convert any video file to audio file with just one click.

Get the latest version of python at https://www.python.org/getit/

## Installation

Currently the script has only been tested on `Debian based OS with Nautilus File Manager`

- Install the latest version of python (3.7.3)

- Install the library moviepy using the below command,

```
  pip3 install moviepy
```

- Copy the `Video_to_Audio.py` file to the location ~/.local/share/nautilus/scripts (.local directory should be hidden, so if you can't find the directory check the `Show Hidden Files` in the settings.)

- Now right click on the file, go to Properties and select the Permissions. Now check the `Allow Executing file as program` dialog box.

     ![Properties Demo Gif](https://github.com/sharma-kunal/Video-To-Audio-Converter/blob/master/demo/demo1.gif)

- Everything is setup now. You can now use the script by right clicking on any video file and selecting Scripts -> Mp4_To_Mp3.py (or whatever the file name is)

     ![PDemo Gif](https://github.com/sharma-kunal/Video-To-Audio-Converter/blob/master/demo/demo.gif)

### NOTE:

Sometimes an error is raised stating that ffmpeg is not found like `No ffmpeg exe could be found. Install ffmpeg on your system, or set the IMAGEIO_FFMPEG_EXE environment variable`. 

There is no need to worry. You just need to run the command,

```
sudo apt install ffmpeg
```

and all the errors would be gone.

If you have any doubts or problems regarding the project, feel free to ask me.

If you want to contribute to the project and make the script for another OS, feel free to contribute to the project.

Happy Coding :)
