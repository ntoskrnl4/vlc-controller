# vlc-controller
Four small scripts to control VLC with your keyboard's native music functions.

## Problem
I had a keyboard that featured dedicated buttons to let you control your music with them. However, the buttons only worked with Windows Media Player, and not my preferred VLC. Solution? AutoHotKey to intercept the keys and run my own programs instead.

## Setup
 - Before you can run the scripts, make sure you have AutoHotKey installed and Python installed, and that `.pyw` files are setup to be executed with pythonw.exe (python without a console window).
 - Then, move the `music_next.pyw`, `music_toggle.pyw`, and `music_previous.pyw` scripts to a convenient directory that makes sense. I placed mine in the `Scripts/` folder within my Python installation folder. You'll need to remember where you put these files, because you're going to...
 - Open up the `music_controls.ahk` file, and update the paths to the scripts. Save and close it. 
 - Optionally, compile the AutoHotKey script (right click on the file) and have Windows run it at launch.
 - The `win10toast` module can be installed to let the script tell you if VLC wasn't open. 
    - If you don't have that module installed, the program will still work, but it won't be able to tell you that VLC wasn't open.

Alright, that's all the setup for the scripts, now to setup VLC:

 - Open VLC and head to `Tools > Preferences`. Go to the advanced settings, and scroll down to `Interface > Main interfaces`. Under "Extra interface modules", click on `telnet`.
 - Expand "Main interfaces" on the left and click on "Lua". Under "Lua Telnet", set the port to `4212` (as of this writing it's the default anyway), and set the password to `vlc`.
 - You'll need to save and restart VLC for the new interface to become active.

## Usage
After running through the setup steps, you should now be able to play a media file, and control it with the native media keys on your keyboard. Two things should be noted here:
 - No other keys can be pressed except the media control key (or keys, if it uses a custom Fn key).
 - If multiple VLC instances are running, this will control the first instance that was started.

And a sidenote, there's no `LICENSE` file on this, but I'm putting this in the public domain - it's merely a couple kilobytes of code and not worth fussing a license over.
