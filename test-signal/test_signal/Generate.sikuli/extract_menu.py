import re
import pytesseract
from PIL import Image


def extract_menu_items(image_path):
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    menu_items = [line.strip() for line in text.split('\n') if line.strip()]
    print(menu_items,text)
    items_in_parentheses = []
    keywords = ["cancel signal", "emergency route"]
    for item in menu_items:
        if not any(keyword in item.lower() for keyword in keywords):
            match = re.search(r'\((.*?)\)', item)
            if match:
                text_in_parentheses = match.group(1)
                items_in_parentheses.append(text_in_parentheses)
    items_in_parentheses = [x.replace('.', '_').replace(' ', '').replace('!', '1') for x in items_in_parentheses]
    return items_in_parentheses

image_path = 'C:\\Users\\anush\\Downloads\\test.sikuli\\s1_menu.png'
items_in_parentheses = extract_menu_items(image_path)
char_map = {
    '!': '1',
    '@': '2',
    '#': '3',
    '$': '4',
    '%': '5'
}
items_in_parentheses = [x.replace('.', '_').replace(' ', '').replace('!', '1') for x in items_in_parentheses]

print(items_in_parentheses)