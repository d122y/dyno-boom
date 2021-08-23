from PIL import Image
import numpy as np
import os
from palette import Palette, TargetPalettes

def Explode(in_path, out_path):
    print("Processing {0}".format(in_path))

    accessories_folders = []
    for f in os.listdir(in_path):
        pathname = "{0}/{1}".format(in_path, f)
        if os.path.isdir(pathname):
            accessories_folders.append(f)
        else:
            base_file_path = pathname
            filename = os.path.splitext(f)[0]

    if not base_file_path:
        print("Couldn't find base image")

    print("Base image {0}".format(base_file_path))
    print("Accessories {0}".format(accessories_folders))
    image = Image.open(base_file_path).convert('RGB')

    # Get the size of the image
    width, height = image.size
    print("Resolution {0}x{1}".format(width, height))

    # Assuming background color solid
    bg_color = image.getpixel( (0,0) )
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
            out_image_filename = "{0}_{1}".format(filename, palette.name)
            out_image_pathname = "{0}/{1}.png".format(out_path, out_image_filename)
            out_image.save(out_image_pathname)

            accessorize(in_path, out_path, accessories_folders, out_image_filename, data)

def accessorize(in_path, out_path, accessories_folders, base_filename, base_image_data):
    for i in range(len(accessories_folders)):
        acc = accessories_folders[i]
        acc_dirpath = "{0}/{1}".format(in_path, acc)
        acc_names = os.listdir(acc_dirpath)
        for acc_name in acc_names:
            acc_pathname = "{0}/{1}".format(acc_dirpath, acc_name)
            acc_filename = os.path.splitext(acc_name)[0]
            print("For {0} appending accessory {1}".format(base_filename, acc_filename))
            acc_image = Image.open(acc_pathname).convert('RGBA')
            out_image = Image.fromarray(base_image_data)
            out_image.paste(acc_image, (0,0), mask=acc_image)
            out_image_filename = "{0}_{1}".format(base_filename, acc_filename)
            out_image_pathname = "{0}/{1}.png".format(out_path, out_image_filename)
            out_image.save(out_image_pathname)

            accessorize(in_path, out_path, accessories_folders[i+1:], out_image_filename, np.array(out_image))