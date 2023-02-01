the_list = [7,4,6,7,4,3,4,3]
def sum_list(the_list):

    somma=0
    if len(the_list)==0:
        return None
    
    for item in the_list:
        
        somma=somma+item
    return somma


q=sum_list(the_list)
#print(q)    
print("la somma di tutti gli elementi è : {}".format(q))
