import torch
import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score, f1_score
from sklearn.metrics import silhouette_score, pairwise_distances
from scipy.spatial.distance import cdist
import joblib
from transformers import BertTokenizer, BertModel
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix

model_path = "model/kmeans_5.pkl"
test_path = "corpus/unlabelled.csv"
result_path = "result/kmeans_5_origin.csv"
tokenizer = BertTokenizer.from_pretrained('bert-base-chinese') 
model = BertModel.from_pretrained('bert-base-chinese', output_hidden_states=True)
kmeans = joblib.load(model_path)
char = '才'

def get_word_vector(text, char):
    tokens = tokenizer.tokenize(text)
    index = tokens.index(char)
    input_ids = tokenizer.convert_tokens_to_ids(tokens)
    input_tensor = torch.tensor([input_ids])
    with torch.no_grad():
        outputs = model(input_tensor)
    hidden_state = outputs.hidden_states[-1][0][index].numpy()
    return hidden_state

df = pd.read_csv(test_path, encoding="utf-8")
text_data = df['text']
#label_data = df['label_meaning']

def change_label(origin_label):
    return origin_label

vector_list = []
for i in range(len(text_data)):
    text = text_data[i]
    #label_data[i] = change_label(label_data[i])
    tensor_tmp = get_word_vector(text, char)
    vector_list.append(tensor_tmp)
vectors = np.array(vector_list)

cluster_labels = kmeans.predict(vectors)
df['label_predicted'] = cluster_labels

df.to_csv(result_path, index=False)

silhouette_avg = silhouette_score(vectors, cluster_labels)
print("轮廓系数:", silhouette_avg)

labels = [0, 1, 2, 3, 4, 5]
intra_cluster_distances = []
for label in labels:
    cluster_data = vectors[cluster_labels == label]
    intra_distance = np.mean(pairwise_distances(cluster_data, metric='euclidean'))
    intra_cluster_distances.append(intra_distance)
    print(f"类别 {label}: 簇内平均距离 {intra_distance}")

# 计算每两个类之间的簇间平均距离
inter_cluster_distances = []
for i in range(len(labels)):
    for j in range(i+1, len(labels)):
        label1 = labels[i]
        label2 = labels[j]
        cluster1_data = vectors[cluster_labels == label1]
        cluster2_data = vectors[cluster_labels == label2]
        inter_distance = np.mean(cdist(cluster1_data, cluster2_data, metric='euclidean'))
        inter_cluster_distances.append(inter_distance)
        print(f"类别 {label1} 和类别 {label2}: 簇间平均距离 {inter_distance}")

# 打印所有类的簇内平均距离和簇间平均距离的均值
print("所有类的簇内平均距离的均值:", np.mean(intra_cluster_distances))
print("所有类之间的簇间平均距离的均值:", np.mean(inter_cluster_distances))

# 计算准确度和F1得分
#accuracy = accuracy_score(label_data, cluster_labels)
#f1 = f1_score(label_data, cluster_labels, average='macro')

#print("准确度：{:.2f}".format(accuracy))
#print("F1得分：{:.2f}".format(f1))
