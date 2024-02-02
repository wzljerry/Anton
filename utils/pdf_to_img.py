from pdf2image import convert_from_path
from PIL import Image
import os

def convert_and_merge_pdf_to_jpg(pdf_path, output_folder):
    """
    Converts a PDF file to JPG images and merges them into a single image.
    The output image is named after the PDF file and saved in the specified folder.
    :param pdf_path: The path to the PDF file.
    :param output_folder: The folder where the merged image will be saved.
    """
    # Extract the base name of the PDF file and construct the output file path
    base_name = os.path.splitext(os.path.basename(pdf_path))[0]
    output_image_path = os.path.join(output_folder, base_name + '.jpg')

    # Convert PDF to a list of images
    images = convert_from_path(pdf_path)

    # Determine the width and total height for the final merged image
    width = max(image.width for image in images)
    total_height = sum(image.height for image in images)

    # Create a new image with the appropriate size for merging
    merged_image = Image.new('RGB', (width, total_height))

    # Paste each image into the merged image
    y_offset = 0
    for image in images:
        # If the image width is not the same as 'width', resize it
        if image.width != width:
            image = image.resize((width, int(image.height * (width / image.width))), Image.ANTIALIAS)
        merged_image.paste(image, (0, y_offset))
        y_offset += image.height
    # Save the merged image
    merged_image.save(output_image_path)
    # Return the merged image path
    return output_image_path

