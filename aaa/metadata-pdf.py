import pikepdf, sys

def main():
    pdf_filename = sys.argv[1]
    pdf = pikepdf.Pdf.open(pdf_filename)
    docinfo = pdf.docinfo
    for key, value in docinfo.items():
        print(key[1:], ":", value)


if __name__ == '__main__':
    try:
        main()
    except Exception:
        print(f"Establece el archivo: {sys.argv[0]} <archivo pdf>")