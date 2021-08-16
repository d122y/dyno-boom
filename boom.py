from PIL import Image
import numpy as np
from palette import Palette, TargetPalettes

def Explode(fileName, sourcePath, outPath):
    print("Processing {0}".format(sourcePath))
    image = Image.open(sourcePath).convert('RGB')

    # Get the size of the image
    width, height = image.size
    print("Resolution {0}x{1}".format(width, height))

    # Assuming background color solid
    bg_color = image.getpixel( (100,100) )
    print("Background color: {0}".format(bg_color))
    print("Background color: {0},{1},{2}".format(bg_color[0],bg_color[1],bg_color[2]))

    outline_color = (0,0,0)
    reflect_color = (255,255,255)
    fore_color = (0,0,0)
    shade_color = (0,0,0)

    # Detecting fore_color, shade_color
    for y in range(height/2, height):
        if fore_color != (0,0,0) and shade_color != (0,0,0):
            break

        for x in range(1, width-1):
            if fore_color != (0,0,0) and shade_color != (0,0,0):
                break

            pixel = image.getpixel( (x,y) )
            if pixel != bg_color and pixel != outline_color and pixel != reflect_color and image.getpixel( (x-1,y) ) == outline_color :
                print("Shade color: {0},{1},{2} as at {3},{4}".format(pixel[0],pixel[1],pixel[2],x,y))
                shade_color = pixel
                continue
            if pixel != bg_color and pixel != outline_color and pixel != reflect_color and image.getpixel( (x-1,y) ) == shade_color :
                print("Fore color: {0},{1},{2} as at {3},{4}".format(pixel[0],pixel[1],pixel[2],x,y))
                fore_color = pixel
                continue

    if fore_color != (0,0,0) and shade_color != (0,0,0):
        for palette in TargetPalettes:
            data = np.array(image)
            red, green, blue = data[:,:,0], data[:,:,1], data[:,:,2]

            fore_mask = (red == [fore_color[0]]) & (green == fore_color[1]) & (blue == fore_color[2])
            data[:,:,:3][fore_mask] = palette.foreColor

            shade_mask = (red == [shade_color[0]]) & (green == shade_color[1]) & (blue == shade_color[2])
            data[:,:,:3][shade_mask] = palette.shadeColor

            bg_mask = (red == [bg_color[0]]) & (green == bg_color[1]) & (blue == bg_color[2])
            data[:,:,:3][bg_mask] = palette.bgColor

            out_image = Image.fromarray(data)
            out_image.save("{0}{1}_{2}.png".format(outPath, fileName, palette.name))