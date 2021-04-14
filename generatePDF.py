import pdfkit 

wkhtmltopdf_path = r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"

config = pdfkit.configuration( wkhtmltopdf = wkhtmltopdf_path)
# web_url = 'https://en.wikipedia.org/wiki/History_of_Python'
web_url = 'https://en.wikipedia.org/wiki/Python_(programming_language)'
pdfkit.from_url(web_url, r'C:\Users\Maki\Desktop\Python_Small_Projects\Convert-HTML-to-PDF\extract2.pdf', configuration=config)