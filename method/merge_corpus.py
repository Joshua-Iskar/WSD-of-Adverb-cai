import pandas as pd
import random
first_corpus = 'corpus/直到.csv'
second_corpus = 'corpus/因为.csv'
third_corpus = 'corpus/只有.csv'
fourth_corpus = 'corpus/为了.csv'
result = "corpus/直到_为了.csv"

df1 = pd.read_csv(first_corpus)
df2 = pd.read_csv(second_corpus)
df3 = pd.read_csv(third_corpus)
df4 = pd.read_csv(fourth_corpus)

# 合并两个数据框
merged_df = pd.concat([df1, df4])

# 将合并后的数据框写入新的csv文件
merged_df.to_csv(result, index=False)
