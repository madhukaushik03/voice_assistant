import pdfplumber
import os
import sys
sys.stdout.reconfigure(encoding='utf-8')


# Path to PDF
pdf_path = os.path.join("..", "data", "tasklist.pdf")  

# Store all extracted text here
all_text = ""

# Open the PDF
with pdfplumber.open(pdf_path) as pdf:
    for page_num, page in enumerate(pdf.pages, start=1):
        text = page.extract_text()
        if text:
            all_text += f"\n--- Page {page_num} ---\n" + text

# # Optional: Print preview
# print("Extracted Text Preview:\n")
# print(all_text[:1000])  # print first 1000 characters

# Save to a .txt file for reference
with open("text.txt", "w", encoding="utf-8") as f:
    f.write(all_text)

print("\n✅ Text extraction complete. Saved as 'text.txt'")
