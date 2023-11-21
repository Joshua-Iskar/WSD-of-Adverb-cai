# Result

## Explanation of Each Senses

| Sense | Explanation |
|------|--------------|
| 0    | for talent and ability |
| 1    | indicate reality not meeting expectations |
| 2    | indicate something happening late |
| 3    | indicate a logical relationship |
| 4    | emphasize a fact |

## Structure of Datasets

### train_1000
| Sense | Quantity |
|------|------|
| 0    | 67   |
| 1    | 168  |
| 2    | 310  |
| 3    | 406  |
| 4    | 49   |

### test_100
| Sense | Quantity |
|------|------|
| 0    | 5    |
| 1    | 17   |
| 2    | 28   |
| 3    | 44   |
| 4    | 6    |

### special
| Senses | Quantity |
|------|------|
| 2    | 28   |
| 3    | 32   |

### Datasets of Weak Labels
| Dataset     | Original Quantity | Quantity after Alignment |
|-----------|-------|-------|
| wèile       | 111   | 52    |
| yīnwèi       | 228   | 108   |
| zhǐyǒu       | 903   | 425   |
| zhídào       | 390   |       |

## Reference Principles for Annotation

| Sense | Principle                  |
|------|-------------------------------------|
| 0    | omitting                                  |
| 1    | gānggāng……cái <br> cái + quantifier <br> cái……jiù |
| 2    | zhídào……cái                            |
| 3    | Condition: zhǐyǒu……cái, chúfēi……cái <br> Purpose: wèile……cái <br> Reason: yīnwèi……cái, zhèngshì……cái, jīngguò……cái |
| 4    | omitting                                  |


## Experimental Results

### Experiment 1
- **Training Method**: unsupervised
- **Training Set**: unlabeled
- **Test Set**: test_100
- **Number of Labels**: 5
- **Model**: kmeans_5
- **Accuracy**: 0.52
- **F1-Score**: 0.60
- **Silhouette Coefficient**: 0.046735667

#### Average Intra-cluster Distance
- Sense 0: 20.02083396911621
- Sense 1: 19.493196487426758
- Sense 2: 18.9094295501709
- Sense 3: 17.55385971069336
- Sense 4: 19.243501663208008

#### Average Inter-cluster Distance
- Sense 0 and Sense 1: 22.225904662232516
- Sense 0 and Sense 1: 22.225904662232516
- Sense 0 and Sense 2: 22.22248905127423
- Sense 0 and Sense 3: 21.684481999488746
- Sense 0 and Sense 4: 21.911078294782175
- Sense 1 and Sense 2: 21.21052104249592
- Sense 1 and Sense 3: 21.560902340645452
- Sense 1 and Sense 4: 20.82405407449749
- Sense 2 and Sense 3: 19.71893907910857
- Sense 2 and Sense 4: 19.800323312255
- Sense 3 and Sense 4: 19.75330325124589

#### Overall Average Distance
- The mean of the average intra-cluster distances for all senses: 19.044165
- The mean of the average inter-cluster distances between all senses: 21.091199710802595

### Experiment 2

- **Training Method**: unsupervised
- **Training Set**: unlabelled
- **Test Set**: test_100
- **Number of Labels**: 3 (cái+/cái-/cái0)
- **Model**: kmeans_3
- **Accuracy**: 0.64
- **F1-Score**: 0.73
- **Silhouette Coefficient**: 0.049815606

#### Average Intra-cluster Distance
- Sense 0: 19.846471786499023
- Sense 1: 19.938364028930664
- Sense 2: 18.51352882385254

#### Average Inter-cluster Distance
- Sense 0 and Sense 1: 22.132111390424345
- Sense 0 and Sense 2: 21.753899285568846
- Sense 1 and Sense 2: 20.306667528410507

#### Overall Average Distance
- The mean of the average intra-cluster distances for all senses: 19.43278821
- The mean of the average inter-cluster distances between all senses: 21.397559401467902

### Experiment 3

- **Training**: supervised
- **Training Set**: train_1000
- **Test Set**: test_100
- **Number of Labels**: 5
- **Model**: model_3_5
- **Epochs**: 5
- **Accuracy**: 0.92
- **F1-Score**: 0.90

### Experiment 4

- **Training Method**: supervised
- **Training Set**: train_1000
- **Test Set**: test_100
- **Number of Labels**: 3 (cái+/cái-/cái0)
- **Model**: model_4_5
- **Epochs**: 5
- **Accuracy**: 0.98
- **F1-Score**: 0.97

### Experiment 5

- **Training Method**: weak supervised
- **Training Set**: zhídào+zhǐyǒu
- **Test Set**: test_100/special
- **Number of Labels**: 2（cái2/cái3）
- **Model**: model_5_5
- **Epochs**: 5
- **test-Accuracy**: 0.86
- **test-F1-Score**: 0.86
- **special-Accuracy**: 0.80
- **special-F1-Score**: 0.80

### Experiment 6

- **Training Method**: weak supervised
- **Training Set**: zhídào+yīnwèi
- **Test Set**: test_100/special
- **Number of Labels**: 2（cái2/cái3）
- **Model**: model_6_5
- **Epochs**: 5
- **test-Accuracy**: 0.85
- **test-F1-Score**: 0.84
- **special-Accuracy**: 0.83
- **special-F1-Score**: 0.83

### Experiment 7

- **Training Method**: weak supervised
- **Training Set**: zhídào+wèile
- **Test Set**: test_100/special
- **Number of Labels**: 2（cái2/cái3）
- **Model**: model_7_5
- **Epochs**: 5
- **test-Accuracy**: 0.76
- **test-F1-Score**: 0.76
- **special-Accuracy**: 0.80
- **special-F1-Score**: 0.80

### Experiment 8

- **Training Method**: weak supervised
- **Training Set**: zhídào+yīnwèi+zhǐyǒu+wèile
- **Test Set**: test_100/special
- **Number of Labels**: 2（cái2/cái3）
- **Model**: model_8_5
- **Epochs**: 5
- **Accuracy**: 0.76
- **F1-Score**: 0.73
- **special-Accuracy**: 0.82
- **special-F1-Score**: 0.81

### Experiment 9

- **Training Method**: supervised
- **Training Set**: train_2_3 （a subset dataset formed from data in train_1000 labeled as 2 and 3）
- **Test Set**: test_100/special
- **Number of Labels**: 2 （cái2/cái3）
- **Model**: model_9_5
- **Epochs**: 5
- **test-Accuracy**: 0.94
- **test-F1-Score**: 0.94
- **special-Accuracy**: 0.73
- **special-F1-Score**: 0.72

## Result Analysis

### Analysis 1
Comparison of 1/3 and 2/4
How much can fine-tuning a pre-trained Bert model improve performance?

### Analysis 2
Comparison of 1/2 and 3/4
Proving or refuting the theory of "cái" in terms of exceeding or falling below expectations

### Analysis 3
Comparison of 3/5~8
The effectiveness of weak supervision in determining the existence of logical relationships

### Analysis 4
Comparison of 5~7
What is the core semantics when "cái" indicates a logical relationship?