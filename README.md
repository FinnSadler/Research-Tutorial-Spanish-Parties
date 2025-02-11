# Research-Tutorial-Spanish-Parties

Pipeline component repository for the Spanish parties research tutorial

# Extract and Preprocess

Extract_and_preprocess is a Python function that takes a raw PDF, converts it to a string, and cleans it by removing formatting characteristics that are typically employed for manifestos (such as bullet points, line breaks, page numbers etc) with RegEx 

## Example Usage

```python
pdf_path = #Path to your PDF here
skip_pages = #Page number that you wish the function to begin extracting from (useful for removing contents pages etc)

Extract_And_Preprocess(pdf_path, skip_pages)

print(cleanedManifesto)
```

# Get Context

Get_Context is a Python function that prepares ```python cleanedManifesto``` for analysis by ManifestoBERTa's context model by creating context strings with neighbouring sentences for each sentence in the text

## Example Usage

```python
pdf_path = #Path to your PDF here
skip_pages = #Page number that you wish the function to begin extracting from (useful for removing contents pages etc)

Extract_And_Preprocess(pdf_path, skip_pages)

print(cleanedManifesto)
```python
Get_Context(sentences, index, maxTokens=200)



