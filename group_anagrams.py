class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapAnagrams=defaultdict(list)
        for i, element in enumerate(strs):
            ascii=0
            alphabets=[0]*26
            for char in element:
                ascii=ord(char)-ord('a')
                alphabets[ascii]+=1
            mapAnagrams[tuple(alphabets)].append(element)
        return list(mapAnagrams.values())
        