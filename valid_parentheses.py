def valid_parentheses(s):
    bracketsMap = {')':'(','}':'{',']':'['}
    stack=[]
    for i in s:
        if i in bracketsMap:
            if not stack and stack.pop()!=bracketsMap[i]:
                return False
        else:
            stack.append(i)
    return True
    
            
                

if __name__== "__main__":
    print(valid_parentheses("(({))"))