'''
Plotting mutational load and allele frequency

Jacob Scott 21 Decemeber 2015

'''
import matplotlib.pyplot as plt
import numpy as np
from pylab import rcParams

my_cmap = plt.cm.get_cmap('nipy_spectral')
my_cmap.set_under('w')

size = 100 #size of the array
time = 100
total_mut1 = np.zeros(size**2)

def sum_digits(digit):
    return sum(int(x) for x in digit if x.isdigit())

path = '../andrea_test/non-stem/text/'

#bit string data
data = open(path+'genomes'+str(time)).read().replace(',','\n').replace('\n','')
x = data.split()
CA = np.array(x).astype('string')
Genomes = np.reshape(CA, (size,size))
genomelength = len(Genomes[0][0])
for entry in range(0, size**2):	total_mut1[entry] = np.array(sum_digits(CA[entry])).astype('int')
mut_array1 = np.reshape(total_mut1, (size,size))

#timepoint 1 clonal evolution
data = open(path+'carriedMutation'+str(time)).read().replace(',','\n').replace('\n','')
x = data.split()
CA = np.array(x).astype('int')
CM1 = np.reshape(CA, (size,size))

rcParams['figure.figsize'] = 10,10

plt.subplot(2,2,1)
# plt.figure()
plt.pcolor(mut_array1, cmap='nipy_spectral', vmin = 0.001)
plt.title('ts '+str(time)+' - mut distance')
plt.colorbar()

plt.subplot(2,2,2)
# plt.figure()
plt.pcolor(CM1, cmap='nipy_spectral', vmin = 0.001)
plt.title('ts '+str(time)+' - unique muts')
plt.colorbar()

plt.subplot(2,2,3)
# plt.figure()
plt.hist(total_mut1, normed=True)
# plt.yscale('log')

plt.subplot(2,2,4)
# plt.figure()
plt.hist(CM1, normed=True)
# plt.yscale('log')
plt.show()