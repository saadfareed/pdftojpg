### Time: 20190904
### Author: YaoLing
### Des: pdf convert to jpg

# -*- coding: UTF-8 -*-
i=0
from pdf2image import convert_from_path #

pdf_name = "/home/sadi/pdf_to_image/Design_Document_Research.pdf"

pages = convert_from_path(pdf_name, 500)
for page in pages:
    jpg_name =str(i) +'.jpg'
    page.save(jpg_name,'JPEG')
    i=int(i)+1