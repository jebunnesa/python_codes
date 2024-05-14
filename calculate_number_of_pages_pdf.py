import PyPDF2


def count_pdf_pages(pdf_path):
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        num_pages = len(pdf_reader.pages)
        return num_pages


# Replace 'your_file.pdf' with the path to your PDF file
pdf_path = 'BRACNet Support Agent Chat - without FAQ.pdf'
page_count = count_pdf_pages(pdf_path)

print(f'The PDF file "{pdf_path}" has {page_count} pages.')
