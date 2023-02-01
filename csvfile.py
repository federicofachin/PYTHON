class CSVFile():

    def __init__(self, name):
        self.name = name

    def get_data(self):

        lista = []
        file = open(self.name, 'r')

        for line in file:
            elements = line.split(",")
            if elements[0] != "Date":
                forma = elements[0]
                value = elements[1]
                lista.append([forma, value])
                #print("elements:{}{}",len(forma),len(value))
        file.close()
        return lista


csv_file = CSVFile("shampoo_sales.csv")
data = csv_file.get_data()  #ho sfruttato la funzione get_data alla classe
print(data)
