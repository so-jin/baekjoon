# f = open("in.txt","r")

# test_num = int(f.readline())
test_num = int(input())
def hex_to_int(str):
    sum = 0
    mul = 1
    for i in range(len(str)-1, -1, -1):
        if ord(str[i])>=65:
            num = ord(str[i])-55
        else:
            num = int(str[i])
        sum+=(num*mul)
        mul*=16
    return sum


for t in range(test_num):
    # square_size, kth = map(int, f.readline().split())
    square_size, kth = map(int, input().split())
    # st = f.readline().replace("\n","")
    st = input().replace("\n","")
    dic = {}
    size =  square_size//4
#     size만큼 밀어가면서 해야한다.

    for i in range(square_size):
        # print(i, i+size)
        if i+size > len(st):
            splited_st = st[i:]
            splited_st += st[:i+size - len(st)]
            int_num = hex_to_int(splited_st)

        else:
            int_num = hex_to_int(st[i:i + size])


        if int_num not in dic:
            # print(int_num)
            dic[int_num] = 1

    dic = sorted(dic.items(), reverse = True)
    # print(dic)
    # for d in dic:
    #     print(hex(d[0]))

    print('#'+str(t+1), dic[kth-1][0])

    # print(st)
