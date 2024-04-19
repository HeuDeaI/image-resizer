from PIL import Image
import argparse
import pathlib



FILE_FOR_SAVING = pathlib.Path(__file__).parent / 'resized_image.png'

		
parser = argparse.ArgumentParser(description='Resize the image')
parser.add_argument('image', type=pathlib.Path, help='The path to the image file.')
parser.add_argument('width', type=int, help='Width of future image')
parser.add_argument('height', type=int, help='Height of future image')

args = parser.parse_args()
width = args.width
height = args.height
file_of_image = args.image.resolve()

with Image.open(file_of_image) as image:
    resized_image = image.resize((width, height), Image.LANCZOS)
    resized_image.save(FILE_FOR_SAVING)
