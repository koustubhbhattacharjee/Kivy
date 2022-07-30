import altair as alt
from vega_datasets import data
import datapane as dp
from matplotlib import pyplot as plt
import numpy as np
from astropy import constants as c, units as u
import pandas as pd

#data=pd.read_csv("Work Functions for Photoelectric Effect.csv",skiprows=7)
#data_dict=data.to_dict()
#print(data)
phi_iron=4.5*u.eV
log_wavelength=np.linspace(1,12,1000)
wavelength=10**log_wavelength*u.nm
freq=(c.c/wavelength).to('Hz')
freq_GHz=freq/1e9

x={"Uranium": 3.6, "Aluminium": 4.08, "Iron": 4.5,"Platinum": 6.35 }
y={val:x[val]*u.eV for val in x}
z={val:(c.h*freq).to('eV')-y[val] for val in y}

#fig,(ax1,ax2,ax3,ax4)=plt.subplots(1,4)
# ax1.plot(z['Uranium'],freq)
# ax1.set_xlabel('KE of photons')
# ax1.set_ylabel(r'$h\nu$')
# ax2.plot(z['Aluminium'],freq)
# ax2.set_xlabel('KE of photons')
# ax2.set_ylabel(r'$h\nu$')
# #fig,(ax3,ax4)=plt.subplots(1,2)
# ax3.plot(z['Iron'],freq)
# ax3.set_xlabel('KE of photons')
# ax3.set_ylabel(r'$h\nu$')
# ax4.plot(z['Platinum'],freq)
# ax4.set_xlabel('KE of photons')
# ax4.set_ylabel(r'$h\nu$')


plt.plot(freq_GHz,z['Uranium'],label=r'U')
plt.plot(freq_GHz,z['Aluminium'],label=r'Al')
plt.plot(freq_GHz,z['Iron'],label=r'Fe')
plt.plot(freq_GHz,z['Platinum'],label=r'Pt')
plt.ylim([0,100])
plt.xlim([0,1E7])
plt.xlabel(r'$\nu$ [frequency(GHz)]')
plt.ylabel(r'KE(eV)')
plt.legend(loc="upper left")
plt.show()
