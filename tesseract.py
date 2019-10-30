import pytesseract

def characterization(image,lang='eng+kor',config='--psm 1 -c preserve_interword_spaces=1'):
    return pytesseract.image_to_string(image, lang, config)