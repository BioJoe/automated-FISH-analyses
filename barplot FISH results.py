#load python included modules
import tkinter as tk
from tkinter import filedialog
#load additional python modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


root = tk.Tk()
root.withdraw()

#parameters to load data
x_axis_name = "genotype"
y_axis_name = "aneuploidy ratio"

#ask for the datafile
file_path = filedialog.askopenfilename(
    title = "Select a compiled FISH results file")
data = pd.read_excel(file_path, index_col=None)
ls_gt = list(data['genotype'].unique())

#create figure
plt.figure(figsize=(4,6))
plt.rcParams.update({'font.size': 18})
ax = plt.subplot(1,1,1)
ax.tick_params(axis='x', which='major', labelsize=10)

#plot mean line and standard deviation errorbars
sns.barplot(x=x_axis_name, y=y_axis_name,
            data=data, errwidth=1, capsize=0.4,
            color="white", ci="sd", linewidth=1,
            edgecolor="black", order = ls_gt)

#plot individual cyst dots
sns.stripplot(x=x_axis_name, y=y_axis_name,
              data=data, jitter=True, color="green",
              size=4, linewidth=0, order = ls_gt)

#format layout
plt.xlabel('')
plt.xticks(rotation=90)
plt.margins(x=None, y=0.2, tight=True)
plt.tight_layout()

#show plot
plt.show()
