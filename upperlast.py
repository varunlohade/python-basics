s= "PythonFLasK"
stri=""
strs=""
for aplha in s:
    if aplha.islower():
        strs=strs+aplha
    elif aplha.isupper():
        stri=stri+aplha

    
print(strs + stri)