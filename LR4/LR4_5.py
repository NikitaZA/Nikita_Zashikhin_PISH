def anagrams(s1, s2):
        if len(s1) != len(s2):
            return False
    
        return sorted(s1) == sorted(s2)

string1 = "listen"
string2 = "silent"
    
print(anagrams(string1, string2))