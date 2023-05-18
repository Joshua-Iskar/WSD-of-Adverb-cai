import pandas as pd

path = 'corpus/test_100.csv'
# 读取CSV文件
df = pd.read_csv(path)

# 选择label值为2或3的行
df_filtered = df.loc[(df['label_meaning'] == 2) | (df['label_meaning'] == 3)]

# 保存结果到新的CSV文件或覆盖原有的CSV文件
df_filtered.to_csv('corpus/test_2_3.csv', index=False)
