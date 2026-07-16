class Solution:
    ans = True
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n==0:
            return True
        count = 0
        if len(flowerbed)==1:
            if n==1 and flowerbed[0]==0:
                return True
            else:
                return False
        if flowerbed[0]==0:
            if flowerbed[1]==0:
                flowerbed[0] = 1
                count+=1
        if flowerbed[-1]==0:
            if flowerbed[-2]==0:
                flowerbed[-1] = 1
                count+=1
        for i in range(1,len(flowerbed)-1):
            if flowerbed[i]==0:
                if flowerbed[i+1]!=1 and flowerbed[i-1]!=1:
                    count+=1
                    flowerbed[i]=1
                if count == n:
                    return True
        if count >= n:
            return True
        return False
                    
                    
        
                
                
        