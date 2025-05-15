import fitz  # PyMuPDF

template_filename = 'V:\\ChristianJ\\Product Label Templates\\ASM Product Label Template.pdf'
output_filename = 'V:\\ChristianJ\\Product Label Templates\\ASM Product Label.pdf'

# Open the PDF and select page
doc = fitz.open(template_filename)
page = doc[0]

# Path to Arial Bold font
font_path = "C:\\Windows\\Fonts\\ariblk.ttf"


# Insert the text with the custom font
page.insert_text(
    (235, 351),                    # X, Y position in points
    "1337-297-01",                 # The text
    fontfile=font_path,           # Path to font file
    fontsize=17.0,                 # Font size
    color=(0, 0, 0)               # RGB color (black)
)

doc.save(output_filename)
print(output_filename)
