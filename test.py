import fitz  # PyMuPDF

template_filename = 'V:\\ChristianJ\\Product Label Templates\\AMAT Product Label Template.pdf'
output_filename = 'V:\\ChristianJ\\Product Label Templates\\AMAT Product Label.pdf'

# Open the PDF and select page
doc = fitz.open(template_filename)
page = doc[0]

# Path to Arial Bold font
font_path = "C:\\Windows\\Fonts\\ariblk.ttf"


# Insert the text with the custom font
page.insert_text(
    (214, 338),                      # X, Y position in points
    "12-203047-01",                 # The text
    fontfile=font_path,           # Path to font file
    fontsize=24.0,                 # Font size
    color=(0, 0, 0)               # RGB color (black)
)

doc.save(output_filename)
