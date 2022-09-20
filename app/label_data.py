import pandas as pd
from db.client import engine
from joblib import load
from db.models.output import Output
from db.client import db
import schedule
import time

def job():
    model = load('models/model.sav')

    input_data = pd.read_sql_table('inputs', engine.connect())
    features = input_data.drop(columns=['id', 'created_at', 'updated_at'], axis=1)
    pred_list = model.predict(features)

    for id, pred_class in zip(input_data['id'],pred_list) :
        iris_instance = Output(id = id, 
                                pred_class=int(pred_class))

        db.add(iris_instance)
        db.commit()

    print(f'Done inserting {len(pred_list)} instances')
    db.close()


schedule.every(1).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)