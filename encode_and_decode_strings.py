class Solution:

    def encode(self, strs: List[str]) -> str:
        result=""
        for element in strs:
            length=len(element)
            result=result+str(length) +"#" +element
        return result
        

    def decode(self, s: str) -> List[str]:
        string=""
        result=[]
        i=0
        while i<len(s):
            j=i
            while j<len(s):
                if s[j]=='#':
                    length=int(s[i:j])
                    string=s[j+1:j+1+length]
                    result.append(string)
                    break
                j+=1
            i=j+length+1
        return result
            
                
