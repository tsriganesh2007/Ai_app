
omit = {"the", "is", "and", "or", "a", "an", "in", "on", "to", "for", "with", "of", "it", "this", "that"}

def tokenizer(text : str):
    temp=""
    final_list=[]
    for letter in text:
        if letter.islower():
            temp+=letter
        elif letter.isupper():
            temp+=letter.lower()
        else:
            if (temp not in omit) and temp:
                final_list.append(temp)
            temp=""
    if (temp not in omit) and temp:
        final_list.append(temp)

    return final_list
