import fitz  # PyMuPDF

template_filename = 'V:\\ChristianJ\\Product Label Templates\\DDI Product Label Template.pdf'
output_filename = 'V:\\ChristianJ\\Product Label Templates\\DDI Product Label.pdf'

# Open the PDF and select page
doc = fitz.open(template_filename)
page = doc[0]

# Path to Arial Bold font
font_path = "C:\\Windows\\Fonts\\calibri.ttf"
custom_font = fitz.Font(fontfile=font_path)
print(custom_font.name)

print(custom_font.name.replace(' ', ''))

prompt1 = 'Part Number: '
pn = input(prompt1)


# Insert the text with the custom font
page.insert_text(
    (195, 427),                      # X, Y position in points
    f'S {pn}',                 # The text
    fontfile="C:\\Windows\\Fonts\\calibri.ttf",           # Path to font file
    fontsize=17.0,                 # Font size
    color=(0, 0, 0)               # RGB color (black)
)

doc.save(output_filename)
print(output_filename)
