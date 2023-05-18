from sklearn.metrics import precision_score, recall_score, f1_score, accuracy_score
import pandas as pd

result_path = "result/kmeans_5.csv"
data = pd.read_csv(result_path, skiprows=1)
# 获取正确标签和预测标签
y_true = data.iloc[:, 1]
y_pred = data.iloc[:, 2]

labels = [0,1,2,3,4]
precision = []
recall = []
f1 = []

for label in labels:
    label_true = (y_true == label)
    label_pred = (y_pred == label)
    precision.append(precision_score(label_true, label_pred))
    recall.append(recall_score(label_true, label_pred))
    f1.append(f1_score(label_true, label_pred))

# 打印每个标签的准确率、召回率和F1值
for i, label in enumerate(labels):
    print(f"Label {label}: Precision = {precision[i]}, Recall = {recall[i]}, F1 = {f1[i]}")