import fitz  # PyMuPDF
from PIL import Image
import io
import os

input_path = ""  # <-- замени на свой путь к файлу
output_path = ""

compressed_doc = fitz.open()
doc = fitz.open(input_path)

for i, page in enumerate(doc):
    print(f"Обработка страницы {i+1}/{len(doc)}...")
    new_page = compressed_doc.new_page(width=page.rect.width, height=page.rect.height)

    # Масштаб 4x для высокого качества
    pix = page.get_pixmap(matrix=fitz.Matrix(4, 4), alpha=False)
    img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

    # JPEG-сжатие с качеством 95%
    buffer = io.BytesIO()
    img.save(buffer, format="JPEG", quality=95)
    buffer.seek(0)

    # Вставка изображения на новую страницу
    rect = fitz.Rect(0, 0, page.rect.width, page.rect.height)
    new_page.insert_image(rect, stream=buffer.read())

# Сохраняем финальный файл
compressed_doc.save(output_path, deflate=True, garbage=4)
compressed_doc.close()
doc.close()

size_mb = os.path.getsize(output_path) / (1024 * 1024)
print(f"✅ Готово! Сжатый файл: {output_path} ({size_mb:.2f} МБ)")
