import collections
import operator

def checkio(text: str) -> str:
    lst = [] 
    final = []
    text = text.lower()
    for i in text:
       # print(i , i.isalpha() )
        if i.isalpha() :
            lst.append(i)
           # print(i,'_append')
    d = dict( collections.Counter(lst) )
    max_value = max(d.values() )

    for i, j in d.items():
        if j == max_value :
            final.append(i)
#            print(j)
#        print (i,j)
#    print(max_value)
    print (min(final) )
#    print (max(d.items(), key=operator.itemgetter(1))[0] )

    #replace this for solution
    return min(final)
