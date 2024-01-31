def merge(arr,start,end):
    mid = start + end //2
    
    len1 = mid-start+1 
    len2 = end-mid
    arr1 = [0]*len1
    arr2 = [0]*len2
    
    mainArrayIndex = start
    for i in range(0,len1):
        arr1[i] = arr[mainArrayIndex]
        mainArrayIndex=mainArrayIndex+1
        
    mainArrayIndex = mid+1
    for i in range(0,len2):
        arr2[i] = arr[mainArrayIndex]
        mainArrayIndex=mainArrayIndex+1
        
 
 
 
        
    index1 = 0 
    index2 = 0
    mainArrayIndex = 0
    
    while(index1 < len1 and index2 < len2):
        if(arr1[index1] > arr2[index2]):
            arr[mainArrayIndex] = arr1[index1]
            index1 = index1 + 1
        else:
            arr[mainArrayIndex] = arr2[index2]
            index2 = index2 + 1 
        mainArrayIndex = mainArrayIndex + 1 
        
    while(index1<len1):
        arr[mainArrayIndex] = arr1[index1]
        index1 = index1 + 1
        mainArrayIndex = mainArrayIndex + 1 
        
    while(index2<len2):
        arr[mainArrayIndex] = arr1[index1]
        index2 = index2 + 1
        mainArrayIndex = mainArrayIndex + 1 
        
            
            



def mergeSort(arr,start,end):
    if(start>=end):
        return
    
    
    mid = (start+end)//2
    # sort left 
    mergeSort(arr,start,mid)
    #sort right
    mergeSort(arr,mid+1,end)
    merge(arr,start,end)





arr = list(map(int,input().split()))
n = len(arr)

mergeSort(arr,0,n-1)