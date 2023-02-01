my_data=[50,52,60]

class Model():
    def fit(self,data):
        raise NotImplementedError('Metodo non implementato')

    def predict(self,data):
        raise NotImplementedError('Metodo non implementato')

class IncrementModel(Model):
    def predict(self,data):

        #prev_value=None
        somma_inc=0
        i=0
        for item in data:
            if i>0:
                somma_inc += data[i]-data[i-1]
            i += 1
        if i<=1:
                return None


        somma_med=somma_inc/(i-1)
        prediction=data[-1]+somma_med
        return prediction

val= [50,52,60]
m=IncrementModel()

#print("Valore prossimo: {}".format(m.predict(val)))