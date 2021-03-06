from PIL import Image
import sys
import urllib.request
#import urllib, cStringIO
import requests
#im = Image.open(requests.get(url, stream=True).raw)

ASCII_CHARS = ['.',',',':',';','+','*','?','%','S','#','@']
#ASCII_CHARS = ['..',',,','::',';;','++','**','??','%%','SS','##','@@']
ASCII_CHARS = ASCII_CHARS[::-1]


'''
method resize():
    - takes as parameters the image, and the final width
    - resizes the image into the final width while maintaining aspect ratio
'''
def resize(image, new_width):
    (old_width, old_height) = image.size
    aspect_ratio = float(old_height)/float(old_width)
    new_height = int((aspect_ratio * new_width)/2)
    new_dim = (new_width, new_height)
    new_image = image.resize(new_dim)
    return new_image
'''
method grayscalify():
    - takes an image as a parameter
    - returns the grayscale version of image
'''
def grayscalify(image):
    return image.convert('L')

'''
method modify():
    - replaces every pixel with a character whose intensity is similar
'''
def modify(image, buckets=25):
    initial_pixels = list(image.getdata())
    new_pixels = [ASCII_CHARS[pixel_value//buckets] for pixel_value in initial_pixels]
    return ''.join(new_pixels)

'''
method do():
    - does all the work by calling all the above functions
'''
def do(image, new_width):
    image = resize(image,new_width)
    image = grayscalify(image)

    pixels = modify(image)
    len_pixels = len(pixels)

    # Construct the image from the character list
    new_image = [pixels[index:index+new_width] for index in range(0, len_pixels, new_width)]

    return '\n'.join(new_image)

'''
method runner():
    - takes as parameter the image path and runs the above code
    - handles exceptions as well
    - provides alternative output options
'''
def Asciify(path,newSize):
    image = None
    IMG=None
    try:
        image = Image.open(path)
    except:
        try:
            urllib.request.urlretrieve(path, 'a.'+path[-3:])
            image = Image.open('a.png')
        except:
            try:
                image = Image.open(requests.get(path, stream=True).raw)
            except:
                print("Unable to find image in",path)
                #print(e)
                return
    image = do(image,newSize)
    return(image)



def asciify(path,newSize):
    IMG=None
    image = None
    try:
        image = Image.open(path)
    except:
        try:
            urllib.request.urlretrieve(path, 'a.'+path[-3:])
            image = Image.open('a.png')
        except:
            try:
                image = Image.open(requests.get(path, stream=True).raw)
            except:
                print("Unable to find image in",path)
                #print(e)
                return
    image = do(image,newSize)
    print(image)
def Version():
    return('Current-2021-07-28')
