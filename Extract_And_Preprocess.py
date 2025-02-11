def Extract_And_Preprocess(pdf_path, skip_pages):
    """
    This function should be used BEFORE passing text to spaCy so sentences can be detected.


    Takes PDF, reads it into Python as text and cleans it:
        - Removes line breaks
        - Removes '.'s
        - Removes bullet points
        - Removes page numbers
        - Removes trailing whitespace
        - Removes double spaces
   
    Args
        - (pdf_path) = path to pdf that you want to extract and clean
        - (skip_pages) = number of pages skipped before extracting


   
    """
    with open(pdf_path, 'rb') as pdf_file:
        reader = PdfReader(pdf_file)
        text = ""
        for i, page in enumerate(reader.pages):
            if i >= skip_pages:
                text += page.extract_text()
    cleanedManifesto = re.sub(r"\n", " ", text)
    cleanedManifesto = re.sub(r"\b\d+[\u2022•]|\u2022|•", "", cleanedManifesto)
    cleanedManifesto = re.sub(r"^\s*\d+\s*$", "", cleanedManifesto, flags = re.MULTILINE)
    cleanedManifesto = cleanedManifesto.strip()
    cleanedManifesto = re.sub(r" {2,}", " ", cleanedManifesto)
    return cleanedManifesto

