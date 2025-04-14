import pandas as pd

dataset = {'Student': ['Joseph','Sally','Henry', 'Lisa','Alex','Michael']
           , 'Grade1': [90,92,37,52,43,65]
           , 'Grade2': [87,43,52,64,57,53]}

df = pd.DataFrame(data=dataset)

df['Outcome'] = df.apply(lambda x: 'Pass' if (x['Grade1'] + x['Grade2'])/2 >= 50 else 'Fail', axis=1)

print(df)