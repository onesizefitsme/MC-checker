import pytesseract


# get answers
custom_config = r'--psm  9'
text = pytesseract.image_to_string('antwoorden7.jpg', config=custom_config)

# create .txt
output_file = open('resultaten.txt','w')
output_file.write(text)
output_file.close()

print(text)



