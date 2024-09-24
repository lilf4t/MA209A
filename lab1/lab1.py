# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 13:56:58 2023

@author: fatima
"""

# uppgift 1. Använd Python för att beräkna;
#(a) 35 ·25 
35*25
#(b) √5 + 1/4 
import numpy as np
np.sqrt(5)+(1/4)
#(c) e^10
import numpy as np
np.exp(10)
#(d) tan(π/6).
import numpy as np
np.tan(np.pi/6)
###############################################################

#uppgift 2. Du har följande utskrift från Python 
#(a) 1.3533e+16 
#(b) 2.1191e-11.
#Skriv båda talen i vanlig form med tiopotenser.
 1.3533 * 10**16
 2.1191 * 10**-11

###############################################################

#uppgift 3. Plotta funktionerna y = sin(x) och y = sin(x) cos(x) i intervallet [0, 10].
# Bägge funktionerna skall plottas i samma figur.
import matplotlib.pyplot as plt
import numpy as np
# ger en vektor med hundra element jämnt fördelade mellan a och b.
x = np.linspace(0,10) 
y1 = np.sin(x)
y2 = np.sin(x)*np.cos(x)
plt.plot(x,y1)
plt.plot(x,y2)
plt.xlabel('x')
plt.ylabel('y')

###############################################################

#uppgift 4. Använd kommando av typen np.arange(a,b,h) för att generera en vektor med värdena
#(a) 10 12 14 16 18 20 22 24 26 28 30 32
import matplotlib.pyplot as plt
import numpy as np
x = np.arange(10,34,2)
print(x)
#(b) -2 -5 -8 -11 -14 -17 -20 -23 -26 -29 -32 -35
x = np.arange(-2,-38,-3)
print(x)

###############################################################

#uppgift 5. Inför funktionen f (x) = 1.2x + √x − 2.
#Plotta funktionen i intervallet [0, 2], sätt ut gridlinjer och skriv axeltext.
#Använd kommandot optimize.fsolve för att bestämma funktionens nollställe.
#Observera att du måste importera biblioteket scipy.optimize
#för att kommandot skall fungera, se Exempel 8.
#När du matar in ett startvärde använd decimalpunkt!
import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as optimize
f = lambda x: 1.2*x + np.sqrt(x) - 2
x = np.linspace(0,2)
y = f(x)
plt.plot(x,y)
plt.grid()
plt.xlabel('x')
plt.ylabel('y')
#genom att kolla på figuren så ser jag att ett nollställe i närheten av x=0.875
x0 = optimize.fsolve(f,0.875)
print(x0) 

###############################################################
#uppgift 6. Inför funktionen f (x) = e−xsin(x). Plotta funktionen i intervallet [0, 6],
#sätt ut gridlinjer och skriv axeltext. Använd kommandot optimize.minimize för att
#bestämma funktionens minpunkt nära x= 4.
#Observera att du måste importera biblioteket scipy.optimize
#för att kommandot skall fungera, se Exempel 8.
import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as optimize
f = lambda x: np.exp(-x) * np.sin(x)
x = np.linspace(0,6)
y = f(x)
plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('y')
#lokalt minpunkt nära x=4
xmin = optimize.minimize(f,4.0)
print(xmin.x)

###############################################################
#uppgift 7. Beräkna integralen 
#med hjälp av kommandot quad.integrate.
#Kontrollera värde genom att beräkna integralen för hand
#(obs denna räkning skall också redovisas under labben).
#Observera att du måste importera biblioteket scipy.integrate,
#se Exempel 9.
import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as integrate
f = lambda x: x**3 + 2*x**2 - x + 1
I = integrate.quad(f, 0, 5)
print(I)



















