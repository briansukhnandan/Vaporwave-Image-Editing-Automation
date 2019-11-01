from PIL import Image, ImageEnhance, ImageDraw, ImageFont, ImageFilter
import random

listOfQuotes = [

    "Wise men don’t judge,\nthey seek to understand.",
    "What the superior man seeks is in \nhimself; what the small man seeks \nis in others.",
    "Nothing ever goes away until it has \ntaught us what we need to know.",
    "Life isn’t as serious as the mind \nmakes it out to be.",
    "Watch what you say, and whatever you say, \npractice it."

]

# Corresponds to Vaporwave font's characters.
listOfChar = ['B','D','I','O','S','U','V','Y','b','d','e','h','k','s','8','9']

def open_image(path):
  newImage = Image.open(path)
  return newImage


# Save Image
def save_image(image, path):
  image.save(path, 'png')


# Create a new image with the given size
def create_image(i, j):
  image = Image.new("RGB", (i, j), "white")
  return image


# Get the pixel from the given image
def get_pixel(image, i, j):
    # Inside image bounds?
    width, height = image.size
    if i > width or j > height:
      return None

    # Get Pixel
    pixel = image.getpixel((i, j))
    return pixel

def convert_Image(image):

    width, height = image.size

    # Create an image in memory and load pixels to get ready for editing
    # RGB values.
    new_image = create_image(width, height)
    pixels = new_image.load()

    #4:3 resolution

    # Loop through every pixel.
    for i in range(width):
        for j in range(height):

            pixel = get_pixel(image,i,j)

            red = pixel[0]
            green = pixel[1]
            blue = pixel[2]

            # print (str(red)+" "+str(green)+" "+ str(blue))

            # Prevent RGB overflow
            if red > 155:
                red=255
            else:
                red += 100

            if blue > 155:
                blue = 255
            else:
                blue += 100

            pixels[i,j] = (red,green,blue)

    # Smooth the image, saturate the color, and add some contrast.
    new_image = ImageEnhance.Contrast(new_image).enhance(1.3)
    new_image = ImageEnhance.Brightness(new_image).enhance(0.6)
    new_image = ImageEnhance.Color(new_image).enhance(2.7)

    # Blur the image with a GaussianBlur, figure out how to configure matrix later.
    new_image = new_image.filter(ImageFilter.GaussianBlur)

    elements_on_image = ImageDraw.Draw(new_image)

    # Set fonts to use as text for our image.
    font = ImageFont.truetype("../fonts/MS-Gothic.ttf",int(width/22))

    vaporfont = ImageFont.truetype("../fonts/Vaporwave.ttf", int(width/3))

    elementQuote = random.choice(listOfQuotes)
    element = random.choice(listOfChar)

    w, h = elements_on_image.textsize(element, font=vaporfont)

    elements_on_image.text((int(width/16),int(height/16)), elementQuote, fill=(0,0,0,127), font=font)

    # In order to center the text, we can subtract the text's width+height from the image's width/height.
    elements_on_image.text((int((width-w)/2),int((height-h)/2)), element, fill=(0, 0, 0), font=vaporfont)

    offset = (width / 2, height / 2)

    return new_image
