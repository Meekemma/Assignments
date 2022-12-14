import pandas as pd
from scipy import stats as st
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

df = pd.read_csv('insurance.csv')
print(df.head)

data=df[["bmi", "age"]].copy()

scaler = MinMaxScaler()
data[["bmi","age"]] = scaler.fit_transform(data[["bmi", "age"]])
print(data)
regression_line = st.linregress(data["bmi"],data["age"])
print(regression_line)
data["bmi_on_graph"] = (data["age"])+ regression_line.intercept
data["error"] = data["bmi_on_graph"]- data["bmi"]
plt.plot(data["age"], data["bmi_on_graph"])
plt.show()
