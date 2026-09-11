from pypdf import PdfReader
from src.cleaner import clean_text
from src.splitter import split_text
import re



pdf_path = "data/ML_Interviews.pdf"

reader = PdfReader(pdf_path)

text = ""

for page in reader.pages:
    page_text = page.extract_text()
    text += page_text + "\n"


cleaned_text = clean_text(text)

chunks = split_text(cleaned_text)


print("Total chunks:", len(chunks))

print("\n--- FIRST CHUNK ---\n")
print(chunks[0])

print("\n--- SECOND CHUNK ---\n")
print(chunks[1])
print("\n--- CHUNK NUMBERS ---\n")
for i, chunk in enumerate(chunks,start =1):
    first_line=chunk.split("\n")[0]
    print(i,"->",first_line)

print("\n--- CHECKING MISSING QUESTIONS ---\n")

for number in range(1, 101):
    found = any(
        chunk.startswith(f"{number}.")
        for chunk in chunks
    )

    if not found:
        print("Missing:", number)

print("\n--- MISSING QUESTIONS TEXT ---\n")

for number in [48, 50, 53, 54, 55, 61, 71, 90, 93]:
    print(f"\n===== QUESTION {number} =====\n")

    pattern = rf"(?s){number}\..*?(?=\n\d+\.\s|\Z)"
    match = re.search(pattern, cleaned_text)

    if match:
        print(match.group(0)[:500])
    else:
        print("Question heading not found")