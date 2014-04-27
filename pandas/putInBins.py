import pandas as pd
import numpy as np

#not initilized data but you get the point
bins = np.arange(0,1020,10)
data['bin_cost'] = bins[np.digitize(data.cost, bins)]
