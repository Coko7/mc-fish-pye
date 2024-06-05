# 🎣 mc-fish-pye

AFK auto-fishing script for Minecraft using Python and OpenCV.

So that you can bake many [fish p*y*es](https://en.wikipedia.org/wiki/Fish_pie) with all the fish you get :)

## ⚙️ Setup

To use this script, you will need to:
- Install Python and the following packages:
  - For `main.py`: [OpenCV](https://pypi.org/project/opencv-python/), [PyAutoGUI](https://pypi.org/project/PyAutoGUI/) and [keyboard](https://pypi.org/project/keyboard/)
  - For `setup.py`: [pynput](https://pypi.org/project/pynput/)
- Run `setup.py` and perform two clicks to define the region of interest
- Update `config.json` to use the newly defined ROI
- Download the [resource pack](./mc-fishpy-pack) and import it
- In game, select the resource pack and then change your in-game language to "Bionic Fisher Lang"
- Make sure you have the [subtitles](https://minecraft.wiki/w/Subtitles) enabled in **Accessibility Settings**
- Also make sure you do not have **Friendly Creatures** sounds muted in your **Sound Settings**
- *Optionally: you can disable the transparency of the subtitle box for better results*

## 📖 Usage

- Launch Minecraft and make sure you have set your language properly
- Run the `main.py` script with root/admin privileges (required for the keyboard key press)
- Quickly switch window focus to Minecraft and let it do the work
- Enjoy an infinite supply of fish and treasure!
- You can stop the script at any moment by holding the `p` key 

## ❓ How it works

This script relies on Minecraft subtitles and a custom language to detect when the fishing bobber sinks.
The custom language sets a few subtitles to be empty and sets the fishing bobber sink subtitle to be a long string.
The long string will cause the black background behind the subtitle text to stretch farther than other subtitles.
These additional black pixels are what the script is looking for to detect if your fishing bobber has caught onto something.
Once a catch is detected, the script sends one right click to retrieve the catch, followed shortly by another one to cast the rod again.
