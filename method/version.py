from transformers import BertModel

model = BertModel.from_pretrained("bert-base-chinese")

print(model.config)