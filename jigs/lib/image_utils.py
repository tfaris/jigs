from PIL import Image


def create_thumbnail(image, width=256, height=256):
    thumbnail_size = (width, height)
    pil_image = image.copy()
    pil_image.thumbnail(thumbnail_size, Image.NEAREST)

    thumb = Image.new('RGBA', thumbnail_size, (255, 255, 255, 0))
    thumb.paste(pil_image,
                ((thumbnail_size[0] - pil_image.size[0]) / 2, (thumbnail_size[1] - pil_image.size[1]) / 2))
    return thumb
