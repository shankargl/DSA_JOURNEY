class Solution:
    def digitSum(self, s: str, k: int) -> str:
    
        while len(s)>k:
            N=len(s)
            new=''
            for i in range(0,N,k):
                if i+k<N:
                    total=0
                    for j in range(i,i+k):
                        total+=int(s[j])
                    new+=str(total)
                    continue
                else:
                    total=0
                    while i<N:
                        total+=int(s[i])
                        i+=1
                    new+=str(total)
            #print(new)
            s=new

        return s
                        

            