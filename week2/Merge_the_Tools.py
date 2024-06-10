def merge_the_tools(string, k):
    # your code goes here
    ans = []
    cnt = 1
    temp_str = []
    for i in string:
        temp_str.append(i)
        if cnt%k == 0:
            strr = list(set("".join(temp_str)))
            ans.append("".join(strr))
            temp_str = []
        cnt+=1
    
    for i in ans:
        print(i)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)