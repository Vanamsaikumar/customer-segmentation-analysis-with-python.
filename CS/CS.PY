import pandas as pd
import math
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline

from datetime import datetime, date
plt.style.use('ggplot')
# Loading the Transactions and Customer Demographics Datasets

trans = pd.read_csv(r'C:\Users\HP\Downloads\Transactions_Cleaned.csv')
cust = pd.read_csv(r'C:\Users\HP\Downloads\NewCustomerList_Cleaned.csv')
# Fetching first 5 transaction records

trans.head(5)

print("Total records (rows) in the Transaction Dataset : {}".format(trans.shape[0]))
print("Total features (columns) in the Transaction Dataset : {}".format(trans.shape[1]))
cust.head(5)
