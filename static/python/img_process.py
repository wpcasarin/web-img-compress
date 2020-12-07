from PIL import Image

def process_img(path, ext, qual):
    if ext in (".jpg", ".jpeg"):
        img = Image.open(path).convert('RGB')
        img.save(f"static/downloads/output{ext}", optimize=True, quality=qual)
    else:
        img = Image.open(path).convert('RGBA')
        img.save(f"static/downloads/output{ext}", optimize=True, quality=qual)


def png_2_jpg(path, ext):
    
    png = Image.open(path).convert('RGBA')
    background = Image.new('RGBA', png.size, (255,255,255))

    alpha_composite = Image.alpha_composite(background, png)
    alpha_composite = alpha_composite.convert('RGB')
    alpha_composite.save('foo.jpg', 'JPEG', quality=100)