import fitz
import os

font_path = "C:\\Users\\cjensen\\Documents\\ddi-cjensen\\product_label_render\\fonts\\calibri.ttf"

if not os.path.isfile(font_path):
    raise FileNotFoundError(f"Font file not found: {font_path}")

doc = fitz.open()
page = doc.new_page()

custom_font = fitz.Font(fontfile=font_path, fontname="CalibriCustom")

page.insert_text(
    (100, 100),
    "Hello from real Calibri!",
    fontname="CalibriCustom",
    fontsize=20,
    color=(0, 0, 0)
)

doc.save("test_calibri_output.pdf")
print("✅ PDF saved as test_calibri_output.pdf")
