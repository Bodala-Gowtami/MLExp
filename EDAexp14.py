#Step 1: Import Necessary Libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Step 2: Load the Dataset
data = pd.read_csv(r"C:\Users\gowta\Downloads\housepredictiondataset\Bengaluru_House_Data.csv")

#Step 3: Initial Data Exploration
print(data.head(10))
print(data.info())

#Step 4: Generate EDA Report
# Make sure ydata-profiling is installed in your environment:
# Run this in your terminal (not in the script): pip install ydata-profiling

from ydata_profiling import ProfileReport
prof = ProfileReport(data)
prof.to_file(output_file='EDA.html')

# If running in Jupyter, you can display the report inline:
# from IPython.core.display import display, HTML
# display(HTML(prof.to_html()))
