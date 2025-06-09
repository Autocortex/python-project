import fitz  # PyMuPDF

doc = fitz.open("")
page = doc[0]
print("Размер страницы в пунктах:", page.rect)
print("Размер в мм:", page.rect.width * 25.4 / 72, "×", page.rect.height * 25.4 / 72)
