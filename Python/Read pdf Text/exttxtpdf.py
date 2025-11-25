import fitz

with fitz.open("test.pdf") as pdf:
    for page in pdf:
        print(page.get_text())

