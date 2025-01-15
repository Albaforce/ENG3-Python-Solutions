
def anagrams(s1:str, s2:str):
    if len(s1) != len(s2) :
        return False
    for i in s1:
        if i in s2:
            s2=s2.replace(i,'',1)   # delete the caractere that is already check with, cause for exemple in the case "tabby", "batty" b is duplicated in the first one, so we should delete it so the second time it check it wont find it so it's false
            continue
        else:
            return False
        
    return True

# or we can solve this problem with only 2 lines 
#def anagrams(s1, s2):
#    return sorted(s1) == sorted(s2) so it's like (("tame", "meta") => "aemt"=="aemt" => True)

print(anagrams("tame", "meta")) # True
print(anagrams("tame", "mate")) # True
print(anagrams("tame", "team")) # True
print(anagrams("tabby", "batty")) # False
print(anagrams("python", "java")) # False






