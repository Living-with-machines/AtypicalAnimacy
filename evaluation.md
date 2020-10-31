# Evaluation results

### _Stories_ dataset

|                                                           | Precision | Recall | F\-score | Map    |
|-----------------------------------------------------------|-----------|--------|----------|--------|
| Most frequent class                                       | 0\.31     | 0\.5   | 0\.383   | 0\.623 |
| SVM TFIDF: targetExp                                      | 0\.911    | 0\.893 | 0\.902   | 0\.928 |
| SVM WordEmb: targetExp                                    | 0\.927    | 0\.919 | 0\.923   | 0\.954 |
| BERTClassifier: targetExp                                 | 0\.951    | **0\.948** | 0\.949   | **0\.985** |
| SVM TFIDF: context3w                                      | 0\.734    | 0\.739 | 0\.737   | 0\.859 |
| SVM WordEmb: context3w                                    | 0\.758    | 0\.742 | 0\.75    | 0\.876 |
| BERTClassifier: context3w                                 | 0\.931    | 0\.926 | 0\.929   | 0\.978 |
| SVM TFIDF: context3wmasked                                | 0\.674    | 0\.677 | 0\.675   | 0\.804 |
| SVM WordEmb: context3wmasked                              | 0\.674    | 0\.678 | 0\.676   | 0\.809 |
| BERTClassifier: context3wmasked                           | 0\.855    | 0\.852 | 0\.854   | 0\.951 |
| SeqModel: LSTM                                            | **0\.952**    | **0\.948** | **0\.95**    | 0\.949 |
| MaskPredict: BERT\-sent, contemporary, weighted, wsdbert  | 0\.739    | 0\.703 | 0\.72    | 0\.848 |
| MaskPredict: BERT\-both, contemporary, weighted, wsdbert  | 0\.839    | 0\.774 | 0\.806   | 0\.892 |
| MaskPredict: BERT\-both, before1850, weighted, wsdbert    | \-        | \-     | \-       | \-     |
| MaskPredict: BERT\-both, timeSensitive, weighted, wsdbert | \-        | \-     | \-       | \-     |

### _19thC Machines_ dataset (animacy)
|                                                           | Precision | Recall | F\-score | Map    |
|-----------------------------------------------------------|-----------|--------|----------|--------|
| Most frequent class                                       | 0\.336    | 0\.5   | 0\.402   | 0\.318 |
| SVM TFIDF: targetExp                                      | 0\.696    | 0\.713 | 0\.704   | 0\.474 |
| SVM WordEmb: targetExp                                    | 0\.694    | 0\.711 | 0\.702   | 0\.499 |
| BERTClassifier: targetExp                                 | 0\.698    | 0\.715 | 0\.706   | 0\.51  |
| SVM TFIDF: context3w                                      | 0\.688    | 0\.71  | 0\.699   | 0\.651 |
| SVM WordEmb: context3w                                    | 0\.728    | 0\.531 | 0\.614   | 0\.481 |
| BERTClassifier: context3w                                 | 0\.695    | 0\.721 | 0\.708   | 0\.721 |
| SVM TFIDF: context3wmasked                                | 0\.592    | 0\.6   | 0\.596   | 0\.498 |
| SVM WordEmb: context3wmasked                              | 0\.518    | 0\.52  | 0\.519   | 0\.339 |
| BERTClassifier: context3wmasked                           | 0\.687    | 0\.696 | 0\.692   | 0\.603 |
| SeqModel: LSTM                                            | 0\.697    | 0\.719 | 0\.708   | 0\.482 |
| MaskPredict: BERT\-sent, contemporary, weighted, wsdbert  | 0\.719    | 0\.742 | 0\.73    | 0\.74  |
| MaskPredict: BERT\-both, contemporary, weighted, wsdbert  | 0\.758    | **0\.778** | 0\.768   | **0\.795** |
| MaskPredict: BERT\-both, timeSensitive, weighted, wsdbert | 0\.758    | 0\.775 | 0\.766   | 0\.777 |
| MaskPredict: BERT\-both, before1850, weighted, wsdbert    | **0\.799**    | 0\.773 | **0\.786**   | 0\.784 |

### _19thC Machines_ dataset (humanness)

|                                                           | Precision | Recall | F\-score | Map    |
|-----------------------------------------------------------|-----------|--------|----------|--------|
| Most frequent class                                       | 0\.434    | 0\.5   | 0\.465   | 0\.155 |
| SVM TFIDF: targetExp                                      | 0\.434    | 0\.499 | 0\.464   | 0\.122 |
| SVM WordEmb: targetExp                                    | 0\.525    | 0\.548 | 0\.536   | 0\.123 |
| BERTClassifier: targetExp                                 | 0\.55     | 0\.588 | 0\.568   | 0\.201 |
| SVM TFIDF: context3w                                      | 0\.545    | 0\.563 | 0\.554   | 0\.213 |
| SVM WordEmb: context3w                                    | 0\.484    | 0\.486 | 0\.485   | 0\.182 |
| BERTClassifier: context3w                                 | 0\.538    | 0\.556 | 0\.547   | 0\.177 |
| SVM TFIDF: context3wmasked                                | 0\.521    | 0\.54  | 0\.53    | 0\.219 |
| SVM WordEmb: context3wmasked                              | 0\.539    | 0\.586 | 0\.562   | 0\.16  |
| BERTClassifier: context3wmasked                           | **0\.6**      | **0\.671** | **0\.633**   | 0\.267 |
| SeqModel: LSTM                                            | 0\.563    | 0\.544 | 0\.554   | 0\.237 |
| MaskPredict: BERT\-sent, contemporary, weighted, wsdbert  | 0\.553    | 0\.612 | 0\.581   | 0\.204 |
| MaskPredict: BERT\-both, contemporary, weighted, wsdbert  | 0\.553    | 0\.613 | 0\.582   | 0\.236 |
| MaskPredict: BERT\-both, timeSensitive, weighted, wsdbert | 0\.587    | 0\.657 | 0\.62    | 0\.249 |
| MaskPredict: BERT\-both, before1850, weighted, wsdbert    | 0\.593    | 0\.664 | 0\.627   | **0\.277** |
