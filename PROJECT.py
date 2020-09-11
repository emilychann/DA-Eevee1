import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Using Dataframe to read Excel file:
Europe = pd.read_excel('IMVA.xlsx')
#print("**************COUNTRIES**************")
# Create a new variable name Europe1, and get all the Europe countries data out from 1978 till 2017
Europe1 = Europe[["Periods", " Belgium & Luxembourg ", " France ", " Germany ", " Italy ", " Netherlands ", " Switzerland ", " United Kingdom "]]
#print(Europe1) # Print Europe2
#print("**************SPLIT**************")
# Create another dataframe by spliting the Europe year and month
Europe2 = Europe1['Periods'].str.split(' ', n=2, expand=True)
#print(Europe2) # Print Europe2
Europe1 = Europe1.assign(Periods=Europe2[0]) # assign a new column named Europe1 with the Year and month in Periods
Europe1 = Europe1.assign(Periods=Europe2[1])
#print("**************CONVERT**************")
Europe1 = Europe1.assign(year=Europe2[1]) # assign a new column named Europe1 with Europe2 in year
Europe1 = Europe1.assign(month=Europe2[2]) # assign a new column named Europe1 with Europe2 in month
#print(Europe1.dtypes) # Print Europe1 data types
Europe1["year"] = pd.to_numeric(Europe1["year"]) # Convert Europe1 "year" data type Object to Numeric
#print("**************TOP 3 COUNTRIES**************")
Europe3 = Europe1[(Europe1["year"] >= 1998) & (Europe1["year"] <= 2007) ] # assign a new column named Europe3 with the "year" between 1998 to 2007 in Europe1
Europe4 = Europe3[[" Belgium & Luxembourg ", " France ", " Germany ", " Italy ", " Netherlands ", " Switzerland ", " United Kingdom "]] # assign a new column named Europe4 with all the Europe countries in Europe3
ps = Europe4.sum().sort_values(ascending=False) # To sort the Europe4 values from descending order and assign it to ps
top3countries = ps.head(3) # assign the top 3 data of ps to top3countries
top3countries.index # Print original indexes
#print(ps)  # Print ps
#print(top3countries)  # Print top3countries
total = top3countries.sum()
mean = round(top3countries.mean(),2)
print("total is ", total)
print("mean is", mean)
#plot the figure
import numpy as np
index = np.arange(len(top3countries.index))
plt.figure(figsize=(10, 10))
plt.xlabel('Countries (Others)', fontsize=10)
plt.ylabel('No. of Travellers (in thousands)', fontsize=8)
plt.xticks(index, top3countries.index, fontsize=7, rotation=60)
plt.title('Top 3 Europe Countries from 1998-2007 (Period 1998-2007)')
plt.bar(top3countries.index, top3countries.values/2800)
#plt.show();

index = np.arange(len(ps.index))
plt.xlabel('Countries (Others)', fontsize=10)
plt.ylabel('No. of Travellers (in thousands)', fontsize=8)
plt.xticks(index, ps.index, fontsize=7, rotation=60)
plt.title('Total Europe Countries from 1998-2017 (Period 1998-2007)')
plt.bar(ps.index, ps.values/2800)
#plt.show();
