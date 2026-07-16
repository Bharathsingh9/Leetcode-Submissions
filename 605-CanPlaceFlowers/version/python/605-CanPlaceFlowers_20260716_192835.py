# Last updated: 7/16/2026, 7:28:35 PM
1class Solution:
2    ans = True
3    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
4        if n==0:
5            return True
6        count = 0
7        if len(flowerbed)==1:
8            if n==1 and flowerbed[0]==0:
9                return True
10            else:
11                return False
12        if flowerbed[0]==0:
13            if flowerbed[1]==0:
14                flowerbed[0] = 1
15                count+=1
16        if flowerbed[-1]==0:
17            if flowerbed[-2]==0:
18                flowerbed[-1] = 1
19                count+=1
20            
21        for i in range(1,len(flowerbed)-1):
22            if flowerbed[i]==0:
23                if flowerbed[i+1]!=1 and flowerbed[i-1]!=1:
24                    count+=1
25                    flowerbed[i]=1
26                if count == n:
27                    return True
28        
29        if count >= n:
30            return True
31        return False
32                    
33                    
34        
35                
36                
37        