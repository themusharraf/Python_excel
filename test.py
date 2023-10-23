import pandas as pd
# pip install pandas==2.1.1

data = {
    'Tolv qilingan sana': ['2023-10-22', '2023-10-23', '2023-10-24'],
    'Qancha kunga': [5, 7, 10]
}


df = pd.DataFrame(data)


df.to_excel('Tolovlar.xlsx', index=False)
