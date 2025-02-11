from transformers import AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained("xlm-roberta-large")

def Get_Context(sentences, index, maxTokens=200):
    """For sentence at position index, create a context string from neighbouring sentences of tokens <= 200"""
    targetSentence = sentences[index]
    targetIds = tokenizer.encode(targetSentence, add_special_tokens = False)
    targetLen = len(targetIds)

    leftIndex = index - 1
    rightIndex = index + 1

    contextTokens = []

    while (leftIndex >= 0 or rightIndex < len(sentences)) and len(contextTokens) < (maxTokens):
        if leftIndex >= 0:
            leftIds = tokenizer.encode(sentences[leftIndex], add_special_tokens = False)
            contextTokens = leftIds + contextTokens
            leftIndex -= 1
        if len(contextTokens) < maxTokens and rightIndex < len(sentences):
            rightIds = tokenizer.encode(sentences[rightIndex], add_special_tokens = False)
            contextTokens = contextTokens + rightIds
            rightIndex += 1
        if len(contextTokens) >= maxTokens:
            break

    if len(contextTokens) > maxTokens:
        contextTokens = contextTokens[:maxTokens]
   
    contextText = tokenizer.decode(contextTokens, skip_special_tokens = True)

    return targetSentence, contextText
