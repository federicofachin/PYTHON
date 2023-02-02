def sum_csv(file_name):
    values=[]   
    file=open(file_name,'r') 
    
    for lines in file:
        elements=lines.split(",")
        if elements[0] != "Date":
            value=elements[1]
            values.append(float(value)) #inserisci i prezzi in un arrey
    file.close()
        
    if(len(values)==0):
        return None
    else:
        return sum(values)
   

#risultato=(sum_csv('shampoo_sales.csv'))
#print('La somma degli elementi è uguale a: {}'.format(risultato))