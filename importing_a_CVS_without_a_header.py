import pandas as pd
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data"
df = pd.read_csv(url, header = None)
path = "D:\python_IBM\importing_1.csv"
df.to_csv(path)