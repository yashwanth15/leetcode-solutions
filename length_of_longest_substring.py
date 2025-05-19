def length_of_longest_substring(s):
    mySet=set()
    left=0
    length=0
    for right,char in enumerate(s):
        while(char in mySet):
            mySet.remove(s[left])
            left+=1
        length=max(length,right-left+1)
        mySet.add(char)
    return length

if __name__== "__main__":
    print(length_of_longest_substring("pwwkew"))