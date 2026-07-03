# Last updated: 7/3/2026, 12:46:23 PM
class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        w_sum=sum(arr[:k])
        count=0
        if w_sum/float(k)>=threshold:
            count+=1
        for i in range(k,len(arr)):
            w_sum+=arr[i]
            w_sum-=arr[i-k]

            if w_sum/float(k)>=threshold:
                count+=1
        return count
        

        