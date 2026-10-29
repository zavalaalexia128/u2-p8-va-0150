import matplotlib.pyplot as plt
import numpy as np

diasX=["lun","Mar","Mie", "Jue", "Vie"]
califa_va_y=[5,6,3,8,20]
plt.bar(diasX,califa_va_y)
plt.title("Califas en VA de Zavala Medina 0150")
plt.xlabel("dias semanal habil")
plt.ylabel("Calificaciones en VA")
plt.grid()
plt.show()
