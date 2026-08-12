# Audio Converter
A Python GUI and CLI Audio Converter, that can convert audio files to MP3 or WAV. Inspired from [PYP2205](https://github.com/PYP2205/Python-Audio-Converter/)

# Requirements
- pydub
- ffmpeg
- tkinter (Windows only)
- tkinterdnd2 0.6.2 (Windows only)
  
# Instructions
- Clone this repository ```git clone https://github.com/KJMazely/Audio-Converter.git``` (or download ZIP and extract)
- Install these Python Packages (as listed above) using the commands below.

**Windows:**
- ```pip install -r requirements.txt```

**Linux:**
- ```pip3 install pydub```
- ```sudo apt-get install ffmpeg```

# Running the program:
There are two different ways to use the program, through a GUI or CLI

## Graphical User Interface (Windows only)
To start the program, run ```python audio_converter.py```

- There are two ways to add the file you want converted, either press the "**Browse...**" button or drag and drop the file onto the field.
- The "**Save to**" field will automatically save the file to the same directory, but can be changed if wanted by clicking the "**Browse...**" button.
- The "**Convert to**" dropdown list has the different extensions you can convert the file to. Click the desired one.
- Press the "**Convert Audio**" button and a warning will show once it has completed/failed.
- The moon/sun button lets you change the application from light to dark mode or vice versa.

## Command Line Interface
When you run this program, you will need to provide a file name in the local directory and a format you want to convert it into.

**Windows:**
- ```python audio_converter.py --file [File Name] --new-format [audio file format]```
  
**Linux:**
- ```python3 audio_converter.py --file [File Name] --new-format [audio file format]```
  
**Example:** 
- ```python audio_converter.py --file audio_file.mp3 --new-format wav``` (Keep in mind that spaces in the file name will break the command, make sure to rename the file to have no spaces beforehand)

### If you want the converted file in a different directory, then add:

**Windows and Linux:**
- ```--output-dir [Path to Directory]```


### If you would like to list the files in the local directory, then run:

**Windows:**
- ```python audio_converter.py --list files```
  
**Linux:** 
- ```python3 audio_converter.py --list files```


### If you want to list the formats you want to convert the file into, then run:

**Windows:**
- ```python audio_converter.py --list formats```
  
**Linux:** 
- ```python3 audio_converter.py --list formats```



# Portable Audio Converter (Windows Only)
If you want to make a portable executable file. Run ```pip install -r portable.txt```, to install packages that can be used to make a portable exe file. This will install "pyinstaller" a CLI program that will make convert a python file into a portable executable. Or you can download an executable from the latest release in the "releases" page.

If you are going to use Pyinstaller, then run

- ```PyInstaller --noconfirm --onedir --windowed --name "Audio Converter" --add-data "convert.py;." --add-data "icons/moon.png;icons" --add-data "icons/sun.png;icons" --collect-all tkinterdnd2 audio_converter.py``` (saves the python app as a portable executable).
- When moving, keep **_internal** in the same directory as the executable


# AI Diclosure
### AI Used for:
- commenting
- dark mode/light mode CSS
