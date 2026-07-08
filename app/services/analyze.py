def analyzer(text : str):
    temp=""
    c=0
    final_dict={}
    for letter in text:
        if letter.islower():
            temp+=letter
        elif letter.isupper():
            temp+=letter.lower()
        elif letter in ["'","-","_"] :
            temp+=letter
        else:
            if temp:
                final_dict[temp]=final_dict.get(temp,0)+1
                c+=1
                temp=""
    if temp:
        final_dict[temp]=final_dict.get(temp,0)+1
        c+=1

    return {
        "total_words" : c,
        "estimated_reading_time_seconds":(c*60)/200,
        "words":final_dict
    }
