# Last updated: 7/16/2026, 7:30:17 PM
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
20        for i in range(1,len(flowerbed)-1):
21            if flowerbed[i]==0:
22                if flowerbed[i+1]!=1 and flowerbed[i-1]!=1:
23                    count+=1
24                    flowerbed[i]=1
25                if count == n:
26                    return True
27        if count >= n:
28            return True
29        return False
30                    
31                    
32        
33                
34                
35        