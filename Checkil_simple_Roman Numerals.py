def checkio(data):
    
    intx = data
    intx = str(intx)
    
    L = [['I', 'IV' , 'IIIII' , 'V' , 'IX'],['X', 'XL' , 'XXXXX' , 'L' , 'XC'] ,['C','CD','CCCCC','D','CM' ]  ,[]  ]
    strO = ''
    for i in range(len(intx)):
        D = ''
        if (len(intx)-i) < 4:
        
            if int(intx[i] ) == 4:
                D = D+ L[len(intx)-i-1][1]
            elif int(intx[i] ) == 9: 
                D = D+ L[len(intx)-i-1][4]
            else: 
                if int(intx[i] ) < 4:
                    for j in range(int(intx[i] ) ):
                        D = D + L[len(intx)-i-1][0]
                    #print(D)    
                else: 
                    for j in range(int(intx[i]) ):
                        D = D + L[len(intx)-i-1][0]
                    D = D.replace(L[len(intx)-i-1][2] , L[len(intx)-i-1][3])
            #print(D)                                
        else: #(len(intx)-i) == 4:
            for j in range(int(intx[i] ) ):
                D = D +'M'
        print(D)
        
        print(i)
        strO =    strO + D     
    print(strO) 
    
    
  
   
    #replace this for solution
    return strO

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(6) == 'VI', '6'
    assert checkio(76) == 'LXXVI', '76'
    assert checkio(499) == 'CDXCIX', '499'
    assert checkio(3888) == 'MMMDCCCLXXXVIII', '3888'