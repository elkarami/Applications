from PIL import Image
import pdf2image

def pdf_to_image(pdf_path, image_path):
    # Convert the PDF file to a list of PIL images
    images = pdf2image.convert_from_path(pdf_path)
    for i, image in enumerate(images):
        # Save each image to a file
        image_file = image_path + str(i) + ".png"
        image.save(image_file, "PNG")

pdf_path = "Flyer A5 JS Print.pdf"
image_path = "./"
pdf_to_image(pdf_path, image_path)