from PIL import Image
import argparse
from typing import Tuple
import sys
# convert.py - Converts a RGB/RGBA image into a PlantUML Sprite.
# Author: Fabio Jun Takada Chino
# This program is licensed under CC0 1.0 Universal


def to_gray16(val: int | Tuple[int]) -> int:
    """
    Converts the given color tuple into a 4-bit grayscale value.    
    """
    val = val[:3]
    total = 0
    for v in val:
        total += v
    total = total / len(val)
    return (int(total) >> 4) & 0xF


def convert(file: str, title: str):
    """
    Loads and converts the image.
    """
    # Load the image
    img = Image.open(file)
    if img.getpalette() is not None:
        raise ValueError('Only RGB images are supported.')

    width = img.width
    height = img.height

    print('@startuml')
    print(f'sprite ${title} [{width}x{height}/16] {{')
    for y in range(0, height):
        line = ''
        for x in range(0, width):
            p = to_gray16(img.getpixel((x, y)))
            line = line + hex(p)[-1:]
        print(line)
    print('}')
    print('@enduml')


def main():
    # Parse the arguments
    parser = argparse.ArgumentParser(
        'convert.py',
        description='Converts a image into a PlantUML sprite.')
    parser.add_argument(
        '--title', '-t',
        dest='title',
        type=str,
        required=True,
        help='Title of the sprite.')
    parser.add_argument(
        '--input', '-i',
        dest='image',
        type=str,
        required=True,
        help='The image file.')

    args = parser.parse_args()

    # Extract the parameters
    title = args.title
    file = args.image

    try:
        convert(file, title)
    except Exception as ex:
        print(str(ex), file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
