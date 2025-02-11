allProbabilities = {}


for sentence, context in sentencesAndContext.items():
    inputs = tokenizer(sentence,
        context,
        return_tensors="pt",
        max_length=300,  
        padding="max_length",
        truncation=True
    )


    logits = model(**inputs).logits


    probabilities = torch.softmax(logits, dim=1).tolist()[0]
    probabilities = {model.config.id2label[index]: round(probability * 100, 2) for index, probability in enumerate(probabilities)}
    probabilities = dict(sorted(probabilities.items(), key=lambda item: item[1], reverse=True))


    allProbabilities[sentence] = probabilities

