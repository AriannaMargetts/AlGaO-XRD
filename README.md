# AlGaO-XRD
Calculating aluminium concentration of (-201) β-(AlxGa1-x)2O3 grown on c-plane sapphire using XRD data
XRD Analysis code
20/7/23

Code was written in Spyder IDE 5.1.5, included in Anaconda.
Python 3.8.12

Code is designed to calculate the aluminium concentration of (-201) monoclinic AlGaO samples through XRD data. Code takes the (-603) peak and returns an output of the aluminium concentration.

Data input:

- Code will take a .csv file of angle (2-theta) and intensity data taken from XRD measurements.
- The .csv file name will need to be manually inputed into the code after the imports and variables.
- The .csv file must have the same filepath as the program.
- The .csv file must have the following format: angle (2-theta) in the first column, intensity in the second column, with NO COLUMN TITLES OR UNITS, just data.
- Data must contain the (-603) XRD peak - that is the peak around 59 degrees. It will not work if given just the (-201) or (-402) peak. The data can contain these peaks, providing (-603) is still given.
- You must know the wavelength that the XRD measurement is taken with. Most likely 1.540598 angstroms. 

Follow the console prompt to input the wavelength of the XRD measurement. Program will print in the console the value of the aluminium concentration. 

Theory behind the code is from the following source: Zhang, W.; Zhang, H.; Zhang, S.; Wang, Z.; Liu, L.; Zhang, Q.; Hu, X.; Liang, H. The Heteroepitaxy of Thick β-Ga2O3 Film on Sapphire Substrate with a β-(AlxGa1−x)2O3 Intermediate Buffer Layer. Materials 2023, 16, 2775. https://doi.org/10.3390/ma16072775
