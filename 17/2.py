import numpy as np
import scipy.io as sio
import pandas as pd

# Importing medical image data into NumPy array
image_data = np.load('path_to_image_file.npy')

# Importing medical image data into SciPy array
image_data = sio.loadmat('path_to_image_file.mat')

# Importing medical image data into Pandas DataFrame
image_data = pd.read_csv('path_to_image_file.csv')
