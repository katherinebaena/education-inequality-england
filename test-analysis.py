
import pandas as pd
import seaborn as sns
import sqlalchemy

data = {
    "School": ["School A", "School B", "School C","School D"],
    "Pupils": [250, 320, 180,450]
}

df = pd.DataFrame(data)

print("My first Data Analyst exercise!")
print(df)
print("\nAverage pupils:", df["Pupils"].mean())
