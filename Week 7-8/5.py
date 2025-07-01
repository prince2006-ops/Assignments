import pandas as pd
import matplotlib.pyplot as plt
data =pd.read_csv('weight_height.csv')
print(data.head())
plt.plot(data['age'], data['height'], marker='o', color='green')
plt.xlabel('Age')
plt.ylabel('Height')
plt.title('Weight vs Height')
plt.plot(data['age'],data['age'],marker='o',color='red')
plt.xlabel('Age')
plt.grid(True)
plt.show()
