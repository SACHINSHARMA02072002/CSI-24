def print_rangoli(size):
    # your code goes here
    patwid=(size*4)-3
    hfpatwid=(patwid+1)//2
    cen=96+size
    hf1pat=chr(cen).rjust(hfpatwid,'-')
    for i in range(size):
        pat2hf=hf1pat[::-1]
        pat2hf=pat2hf[1:]
        print(hf1pat+pat2hf)
        hf1pat=hf1pat[2:]
        cen-=1
        hf1pat+='-'
        hf1pat+=chr(cen)
    #adjustment
    hf1pat=chr(cen+size)+'-'+hf1pat[:-2]
    #bottom
    for j in range(size-1):
        hf1pat=hf1pat[:-2]
        hf1pat='--'+hf1pat
        pat2hf=hf1pat[::-1]
        pat2hf=pat2hf[1:]
        print(hf1pat+pat2hf)

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)