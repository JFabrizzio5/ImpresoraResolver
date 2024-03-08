import os
import sys
import subprocess


def install(package):
    subprocess.run([sys.executable, "-m", "pip", "install", package], check=True)

try:
    import img2pdf
    import tkinter as tk
    from tkinter import filedialog
except ImportError:
    install('img2pdf')
    install('tkinter')

def convert_to_pdf():
    # Get the PDF name
    pdf_name = pdf_name_entry.get()

    # Get the selected image directory
    image_dir = image_dir_entry.get()

    # Get the selected PDF save directory
    pdf_save_dir = pdf_save_dir_entry.get()

    # Step 1: List all image files in the directory
    image_files = [f for f in os.listdir(image_dir) if f.endswith(('.png', '.jpg', '.jpeg')) and 'scan' in f.lower()]

    # Step 2: Sort the list of image files based on the numerical order of their names
    sorted_image_files = sorted(image_files, key=lambda x: int(''.join(filter(str.isdigit, x))))

    # Step 3: Use the img2pdf library to convert the sorted list of image files into a PDF
    with open(os.path.join(pdf_save_dir, pdf_name + '.pdf'), 'wb') as f:
        f.write(img2pdf.convert([open(os.path.join(image_dir, i), 'rb').read() for i in sorted_image_files]))

def select_image_folder():
    selected_folder = filedialog.askdirectory()
    image_dir_entry.delete(0, tk.END)
    image_dir_entry.insert(0, selected_folder)

def select_pdf_save_folder():
    selected_folder = filedialog.askdirectory()
    pdf_save_dir_entry.delete(0, tk.END)
    pdf_save_dir_entry.insert(0, selected_folder)

root = tk.Tk()
root.title("Convert Images to PDF")
root.geometry("500x300")  # Set the initial window size

tk.Label(root, text="Nombre del PDF:").pack()
pdf_name_entry = tk.Entry(root)
pdf_name_entry.pack()

tk.Label(root, text="Folder de imagenes:").pack()
image_dir_entry = tk.Entry(root)
image_dir_entry.pack()

select_image_dir_button = tk.Button(root, text="Selecciona folder", command=select_image_folder)
select_image_dir_button.pack()

tk.Label(root, text="Folder donde quieres guardar el pdf:").pack()
pdf_save_dir_entry = tk.Entry(root)
pdf_save_dir_entry.pack()

select_pdf_save_dir_button = tk.Button(root, text="Selecciona", command=select_pdf_save_folder)
select_pdf_save_dir_button.pack()

convert_button = tk.Button(root, text="Converitr a pdF", command=convert_to_pdf)
convert_button.pack()

# Added label at the bottom
github_label = tk.Label(root, text="Github: Jfabrizzio5")
github_label.pack(side=tk.BOTTOM)

root.mainloop()
