import pandas as pd
from db.models.input import Input
import uuid
from db.client import db


data = pd.read_csv('data/iris.csv')

for _, row in data.iterrows():
    
    iris_instance = Input(id = str(uuid.uuid4()), 
                            sepal_length=row['SepalLengthCm'], 
                            sepal_width=row['SepalWidthCm'],
                            petal_length=row['PetalLengthCm'], 
                            petal_width=row['PetalWidthCm'])
    db.add(iris_instance)
    db.commit()

print(f'Done inserting {len(data)} instances')
db.close()
