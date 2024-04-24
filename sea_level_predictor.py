import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
  df = pd.read_csv ('epa-sea-level.csv')


    # Create scatter plot
  x = df ['Year']
  y = df ['CSIRO Adjusted Sea Level']
  fig, axes = plt.subplots (figsize = (7,7))
  plt.scatter (x,y)

    # Create first line of best fit
  result= linregress (x,y)
  print (result)
  x_first_line = pd.Series ([i for i in range(1880, 2051)])
  y_first_line = (result.slope * x_first_line) + result.intercept
  plt.scatter (x,y)
  plt.plot (x_first_line, y_first_line, color = 'r')


    # Create second line of best fit
  df_future_sea_level = df.loc [df['Year']>=2000]
  x_future_sea_level = df_future_sea_level ['Year']
  y_future_sea_level = df_future_sea_level ['CSIRO Adjusted Sea Level']

  result2= linregress (x_future_sea_level, y_future_sea_level)

  x_second_line = pd.Series ([i for i in range (2000, 2051)])
  y_second_line = (result2.slope * x_second_line)+ result2.intercept
  plt.plot (x_second_line, y_second_line, color = 'g')

  plt.title ('Rise in Sea Level', fontsize = 16)
  plt.xlabel ('Year',fontsize = 14)
  plt.ylabel ('Sea Level (inches)', fontsize = 14)


    # Add labels and title

    
    # Save plot and return data for testing (DO NOT MODIFY)
  plt.savefig('sea_level_plot.png')
  return plt.gca()