class CSVFile():
    def __init__(self, name):
        self.name=name

        #provo ad aprirlo e leggere una riga
        self.can_read= True
        try:
            file=open(self.name,'r')
            file.readline()
        except Exception as e:
            self.can_read =False
            print('Errore in apertura del file: ""{}"'.format(e))
            
    def get_data(self):
        if not self.can_read:
            #se nell'init ho settato can_read a false vuol dire che il file non poteva essere aperto o era illeggibile
            print('Errore, file non aperto o illeggibile')

            #esco dalla funzione tornando "niente"
            return None

        else:
            #inizializzo una lista vuota per salvare tutti i dati
            lista=[]
            #apro il file
            file=open(self.name,'r') 

            #leggo il file linea per linea
            for line in file:
                #faccio lo split di ogni linea sulla virgola
                elements=line.split(",")

                #posso anche pulire il carattere di newline
                #dall'ultimo elemento con la funzione strip():
                elements[-1]=elements[-1].strip()

                #p.s. in realtà strip() toglie anche gli spazi bianchi all'inizio e alla fine di una stringa

                #se NON sto processando l'intestazione...
                if elements[0] != 'Date':
                    #aggiungo alla lista gli elementi di questa linea
                    lista.append(elements)
        file.close()
        return lista
class  NumericalCSVFile(CSVFile):

    def get_data(self):
        #chiamo la get_data del genitore
        string_data = super().get_data()
        

        #preparo una lista per contenere i dati ma in formato numerico
        numerical_data = []

        #ciclo su tutte le "righe" corrispondenti al file originale
        for string_row in string_data:
            # preparo una lista di supporto per salavare la riga in "formato" numerico (tranne il primo elemento)
            numerical_row = []

            #ciclco su tutti gli elementi della riga con un enumeratore: cosi' ho gratis l'indice "i" della posizione dell'elememto nella riga
            for i,element in enumerate(string_row):

                if i==0:
                    #il primo elemento della riga lo lascio in formato stringa 
                    numerical_row.append(element)
                else:
                    #converto a float tutto gli altri. Ma se fallisco, stampo l'errore e rompo il ciclo (e poi salterò la riga)
                    try:
                        numerical_row.append(float(element))
                    except Exception as e:
                        print ('Errore in conversione del valore "{}" a numerico: "{}"'.format(element, e)) # e è l'errore del computer
                        break

            #alla fine aggiungo la riga in formato numerico alla lista "esterna" ma solo se sono riuscito a processare tutti gli elementi. Qui controllo per la lunghezza, ma avrei anche potuto usare una variabile di supporto o fare due break in cascata
            if len(numerical_row) == len(string_row):
                numerical_data.append(numerical_row)

        return numerical_data

csv_file_numerico=NumericalCSVFile('shampoo_sales.csv')
data=csv_file_numerico.get_data()
print(data)


