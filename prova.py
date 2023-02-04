my_list= ['marco','irene','luigi']
trova='marco'
if trova in my_list: 
    print('trovato {}'.format(trova))


my_dict ={'Trieste': 34100, 'Padova':33200, 'Udine':11000}
print('il CAP di Trieste è: {}'.format(my_dict['Trieste']))


my_var=4
your_var=3

if(my_var > your_var):
    print("my var è più grande della tua")
    if (my_var - your_var) <= 1:
         print("... ma non così tanto")
    elif (my_var - your_var) <= 5:
        print("... abbastanza")
    else:
        print("... molto")
#se metto tre if entra in tutti e tre a prescindere se è già entrato in altri precedentemente
#con if elif ed else entra solo in uno dei tre
            
            