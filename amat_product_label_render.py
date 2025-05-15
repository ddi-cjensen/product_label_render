import fitz  # PyMuPDF

template_filename = 'V:\\ChristianJ\\Product Label Templates\\AMAT Product Label Template.pdf'
output_filename = 'V:\\ChristianJ\\Product Label Templates\\AMAT Product Label.pdf'

# Open the PDF and select page
doc = fitz.open(template_filename)
page = doc[0]

# Path to Arial Bold font
font_path = "C:\\Windows\\Fonts\\ariblk.ttf"
prompt1 = 'AMAT Part Number: '

pn = input(prompt1)
prompt2 = f'AMAT Rev for {prompt1}: '
rev= input(prompt2)

# Insert the text with the custom font
page.insert_text(
    (235, 351),                      # X, Y position in points
    pn,                 # The text
    fontfile=font_path,           # Path to font file
    fontsize=17.0,                 # Font size
    color=(0, 0, 0)               # RGB color (black)
)

# Insert the text with the custom font
page.insert_text(
    (425, 351),                      # X, Y position in points
    rev,                 # The text
    fontfile=font_path,           # Path to font file
    fontsize=17.0,                 # Font size
    color=(0, 0, 0)               # RGB color (black)
)

doc.save(output_filename)
print(output_filename)
