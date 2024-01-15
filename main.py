from PIL import Image
from reportlab.pdfgen import canvas
import os

def convert_images_to_pdf(parent_folder, output_pdf_path):
    for folder_name in os.listdir(parent_folder):
        folder_path = os.path.join(parent_folder, folder_name)

        if os.path.isdir(folder_path):
            # Get all JPG files in the specified folder
            jpg_files = [file for file in os.listdir(folder_path) if file.lower().endswith('.jpg')]

            if not jpg_files:
                print(f"No JPG files found in {folder_path}")
                continue

            # Sort the files based on their names
            jpg_files.sort()

            # Create a PDF file with the folder name
            pdf_path = os.path.join(output_pdf_path, f"{folder_name}.pdf")
            pdf_canvas = canvas.Canvas(pdf_path)

            for idx, jpg_file in enumerate(jpg_files):
                # Open each JPG file and convert it to RGB mode
                img_path = os.path.join(folder_path, jpg_file)
                img = Image.open(img_path).convert('RGB')

                # Get the size of the image (assuming all images have the same size)
                width, height = img.size

                # Add a page to the PDF with the same size as the image, starting from the second image
                if idx > 0:
                    pdf_canvas.setPageSize((width, height))
                    pdf_canvas.showPage()

                # Draw the image on the PDF page
                pdf_canvas.drawInlineImage(img, 0, 0, width, height)

            # Save the PDF file
            pdf_canvas.save()
            print(f"PDF file saved at: {pdf_path}")

if __name__ == "__main__":
    parent_folder = input("Enter the path of the parent folder containing subfolders with JPG files: ")
    output_pdf_path = input("Enter the path where you want to save the PDFs: ")

    convert_images_to_pdf(parent_folder, output_pdf_path)
