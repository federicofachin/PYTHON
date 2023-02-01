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
        if not self.can_read: #se non è leggibile
            #se nell'init ho settato can_read a false vuol dire che il file non poteva essere aperto o era illeggibile
            print('Errore, file non aperto o illeggibile')

            #esco dalla funzione tornando "niente"
            return None

        else: #se è leggibile
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
csv_file=CSVFile("shampoo_sales.csv")
data=csv_file.get_data()
print(data)