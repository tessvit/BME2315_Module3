# ligand_receptor.py

import numpy as np
import matplotlib.pyplot as plt

# Function to calculate fractional receptor activation with two ligands (GLP1 and Semaglutide)
def Fact(glp1, sema, kd1GLP1, kd2Sema):
    """Fractional receptor activation with two ligands (GLP1 and Semaglutide): Kd2*G+Kd1*S/(Kd1*Kd2+Kd2*G+Kd1*S)""" # where G is concentration of GLP1 and S is concentration of Semaglutide. Kd1 is the dissociation constant for GLP1 and Kd2 is the dissociation constant for Semaglutide.
    return (kd2Sema*glp1+kd1GLP1*sema)/(kd1GLP1*kd2Sema+kd2Sema*glp1+kd1GLP1*sema)

# Defining variables for ligand concentrations and dissociation constants
glp1Fast = 0.0150                  # ligand concentration for GLP1 after fasting, from slide 15; this graph can also be used to show the effect of GLP1 after meal by changing the value to the ligand concentration for GLP1 after meal, which is 0.040 [nM]
sema = np.logspace(-2, 4, 500)     # ligand concentration for semaglutide (range from 0.01 to 10,000 [nM])
kd1GLP1 = 0.17                       # dissociation constant for GLP1, from slide 15 [nM]
kd2Sema = 0.38                       # dissociation constant for Sema, from slide 15 [nM]

plt.figure()
plt.semilogx(sema, Fact(glp1Fast, sema, kd1GLP1, kd2Sema), lw=2, label="GLP1 After Fasting") # Creates line on graph for the Fact using the GLP1 after fasting ligand concentration
plt.axhline(0.5, ls="--", c="gray", lw=1) # Creates horizontal line on graph at 0.5 to show 50% activation point
plt.axvline(kd2Sema, ls="--", c="gray", lw=1, label=f"Semaglutide Kd = {kd2Sema} nM") # Creates vertical line on graph at the dissociation constant for Semaglutide
plt.ylim(0, 1)
plt.xlabel("Semaglutide Concentration [S] (nM)") # Creates x-axis label
plt.ylabel("Fraction active (Fact)") # Creates y-axis label
plt.legend()
plt.show()