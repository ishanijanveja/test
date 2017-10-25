import time

######THIS FEELS GREAT!!!!!######

def split(n):
    arr = []
    if(not(n==1)):
        for i in range(1,n):
            arr.append([n-i,i])

        # if n%2==0 :
        #     for i in range(1,(n/2)+1):
        #         arr.append([n-i,i])
        # else:
        #     for i in range(1,(n/2)+1):

        #         arr.append([n-i,i])
    return arr

def split_n_array(array):
    n = len(array)
    mini_array=[]
    new_array=[]
    for i in range(0,n):
        mini_array.append(split(array[i]))
    possibilities = []
    breaker = 0
    for i in range(len(mini_array[0])):
        a = mini_array[0][i]
        possibilities.append([a[0],a[1]])
#        print ("poss",possibilities)
        for j in range(1,len(mini_array)):
            if breaker == 1:
                breaker = 0
                break
            for k in range(len(mini_array[j])):
                if (possibilities[i][-1]==mini_array[j][k][0]):
                    possibilities[i].append(mini_array[j][k][1])
                    break
                elif k == len(mini_array[j]):
                    breaker = 1
    new_layer = []
    for lists in possibilities:
        if (len(lists)==(len(mini_array)+1)):
            global count
            count = count + 1
            new_layer.append(lists)

    return  new_layer

# print(split_n_array([2,2]))

def main(array_input):

    if (not(array_input == [])):
        new_array_input = split_n_array(array_input)
        for arrays in new_array_input:
            print arrays
            main(arrays)



count = 1
main([9])
print(count)
