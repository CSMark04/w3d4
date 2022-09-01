# excercise 1
words = ['this' , 'is', 'a', 'sentence', '.']

def swap(alist,x,y,z,a):
    alist[z],alist[x],alist[y],alist[a] = alist[z],alist[y],alist[x],alist[a]
    return alist[::-1]

swap(words, 0,1,2,3)



# excercise 2

a_text = 'In computing, a hash table hash map is a data structure which implements an associative array abstract data type, a structure that can map keys to values. A hash table uses a hash function to compute an index into an array of buckets or slots from which the desired value can be found'

def countsDis(arr):
    counter = dict()

    for word in arr.split():
        if word in counter:
            counter[word] += 1
        else:
            counter[word] = 1
    return counter

countsDis(a_text)


#excercise 3

list1 = [5,2,6,235,52,64,21,553]
target = 2

if target in list1:
    print('target here')
else:
    print('not here')


# linear time complexity