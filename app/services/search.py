def searcher(word:str,records: list[str]):
    word=word.lower()
    final_list=[]
    for text in records:
        c=0
        temp=""
        for letter in text:
            if letter.islower():
                temp+=letter
            elif letter.isupper():
                temp+=letter.lower()
            elif letter in ["'","-","_"] :
                temp+=letter
            else:
                if temp==word:
                    c+=1
                temp=""
        if temp==word:
            c+=1
        if c>0 :
            final_list.append({
                "record":text,
                "matches":c
            })
    def sort_helper(dict):
        return dict["matches"]
    return sorted(final_list,key=sort_helper,reverse=True)
