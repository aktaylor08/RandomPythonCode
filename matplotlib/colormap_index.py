#/usr/bin/env python
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.cm as cmx

#define number of colors to use
N_COLORS = 5

#create the values
values=(range(N_COLORS))

#colormap
jet = cm = plt.get_cmap('jet') 
#normilze and create map
cNorm  = colors.Normalize(vmin=0, vmax=values[-1])
scalarMap = cmx.ScalarMappable(norm=cNorm, cmap=jet)

fig, ax = plt.subplots()
for i in range(N_COLORS):
    #get the index here by calling to_rgba(i)
    ax.scatter([i],[i], c=scalarMap.to_rgba(i), label='C' + str(i))
ax.legend(loc='upper left')
plt.show()


