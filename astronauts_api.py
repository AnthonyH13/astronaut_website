#importing modules needed for data visualization

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

%matplotlib inline

# change plotting colors per client request
plt.style.use('ggplot')

# Increase default figure and font sizes for easier viewing.
plt.rcParams['figure.figsize'] = (8, 6)
plt.rcParams['font.size'] = 14

astro = pd.read_csv('/Users/anthony/Desktop/flask_app/astronaut-yearbook.zip')

astro.head(3)
