def average(array):
    # your code goes here
    total = 0
    set1 = set(array)  
    for i in set1:
        total += i  
        
    return total/len(set1) 
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)