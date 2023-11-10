# converter

## Description

**Converter** is a small Python tool that can load a 16-color image file and 
convert it into a PUML file.

## Dependencies

This program requires Python 3.11 or later and the dependencies defined in the 
file `dependencies.txt`. We strongly recommend you to use a Python venv as it
will keep your system's installation clear from useless dependencies required
by this program.

Use `pip install -r requirements.txt` to install all required dependencies.

## Preparing the image

This program takes as its input a RGB/RGBA image file in one of the formats
supported by Pillow. We suggest the usage of PNG or BMP because they are lossless
image formats.

The image will be interpreted as a alpha values where black is fully transparent
and white is fully opaque.

To achieve the best results, we suggest the usage of SGV images exported to the
final size of the sprite, using black as the background and whie for the
foreground.

## Running the program

To run this program, just use:

```
python convert.py -i <image file> -t <icon title>
```

The contents of the sprite will be outputed to the stdout of the terminal.
