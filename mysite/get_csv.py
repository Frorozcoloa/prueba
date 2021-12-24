import pandas as pd
from num.models import Num

def get_csv():
    values = Num.objects.all()
    df=pd.DataFrame(list(values.values()))
    df.to_csv("NEU.csv", index=False)

get_csv()