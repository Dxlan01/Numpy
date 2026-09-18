import numpy as np
#5 productos en dolares
precios_usd = np.array([10, 25, 50, 7.5, 100])
#Los queremos convertir a pesos 
precios_cop = precios_usd * 4000
#Numpy multiplica TODO sin necesidad de un ciclo for
print("Precios en USD:", precios_usd)
print("Precios en COP:", precios_cop)
