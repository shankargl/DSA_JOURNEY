class Solution:
    def kthCharacter(self, k: int) -> str:
        char=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

        word='a'
        while len(word)<k:
            con=''
            for i in word:
                ind=char.index(i)
                con+=char[ind+1]
            word+=con
        return word[k-1]


