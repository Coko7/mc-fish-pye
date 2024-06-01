# mc-fishpy

AFK auto-fishing script for Minecraft using Python and OpenCV

## Setup

To use this script, you will need to:
- Install Python and the following packages: PyAutoGUI, OpenCV and Keyboard
- Download the given resource pack and add it to your game
- Set your in-game language to "Bionic Fisher Lang"
- Make sure you have subtitles enabled in Accessibility settings
- *You can optionally disable the transparency of the subtitle box for better results*

## Usage

- Launch Minecraft and make sure you have set your language according to the Setup.
- Run the script with administrator privileges (required for the keyboard key press)
- Enjoy an infinite supply of fish and treasure!
- You can press `q` to stop the script

## How it works

This script relies on Minecraft subtitles and custom language to detect when the fishing bobber sinks.
The custom language sets a few subtitles to be empty and sets teh fishing bobber sinking subtitle to be a long string.
The long string for the subtitle will cause the black background behind it to stretch farther than other subtitle boxes.
These additional black pixels are what the script is looking for to detect if your fishing bobber has caught something.
Once a catch is detected, the script sends one right click to retrieve the catch, followed shortly by another one to cast the rod again.
