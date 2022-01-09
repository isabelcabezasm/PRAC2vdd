# The following code to create a dataframe and remove duplicated rows is always executed and acts as a preamble for your script: 

import matplotlib.pyplot as plt
import pandas as pd


import random
import numpy
from matplotlib import pyplot

hombres = dataset[(dataset.SEXO == 1)]
mujeres = dataset[(dataset.SEXO == 6)]


plt.hist([hombres['Precio/Hora'], mujeres['Precio/Hora']], bins=20, color=['#118DFF','#12239E'], label=['Hombres', 'Mujeres'])
pyplot.legend(loc='upper right')
pyplot.show()
