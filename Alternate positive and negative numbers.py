#Given an unsorted array Arr of N positive and negative numbers. Your task is to create an array of alternate positive and negative numbers without changing the relative order of positive and negative numbers.
class Solution:
    def rearrange(self,arr, n):
        # code here
        negative=[]
        positive=[]
        
        for i in range(n):
            if arr[i]<0:
                negative.append(arr[i])
            else:    
                positive.append(arr[i])
            
        i=0
        j=0
        k=0
        
        
        while i<len(positive) and j<len(negative):
            arr[k]=positive[i]
            k=k+1
            i=i+1
            
            arr[k]=negative[j]
            k=k+1
            j=j+1
            
            
        while i < len(positive):
            arr[k] = positive[i]
            k += 1
            i += 1

        while j < len(negative):
            arr[k] = negative[j]
            k += 1
            j += 1
            
        return arr