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

Get_Context is a Python function that prepares ```cleanedManifesto``` for analysis by ManifestoBERTa's context model by creating context strings with neighbouring sentences for each sentence in the text. Sentences must first be detected with SpaCy's Spanish transformer model and saved as a list

## Example Usage

```python
sentencesAndContext = {}

for i in range(len(stringSentences)):
    sentence, context = Get_Context(stringSentences, i, maxTokens=200) 
    sentencesAndContext[sentence] = context
```

# Run ManifestoBERTa

Run_ManifestoBERTa is the recommended method for implementing Manifesto Project's [ManifestoBERTa context model](https://huggingface.co/manifesto-project/manifestoberta-xlm-roberta-56policy-topics-context-2024-1-1), and is not original code





