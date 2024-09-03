from PIL import Image, ImageFilter

def apply_filter(image_path, filter_type):
    image = Image.open(image_path)
    if filter_type == "BLUR":
        return image.filter(ImageFilter.BLUR)
    elif filter_type == "CONTOUR":
        return image.filter(ImageFilter.CONTOUR)
    # Add more filters as needed
    return image
