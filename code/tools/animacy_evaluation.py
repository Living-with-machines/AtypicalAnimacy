from sklearn.metrics import precision_score
from sklearn.metrics import recall_score


def animacy_score(predicted,scores,weighted,res_cutoff):

    tmp_pred = []
    tmp_scor = []
    for x in range(len(predicted)):
        if not predicted[x] == None: # Keep only 0-1 animacy values for the prediction
            tmp_pred.append(int(predicted[x]))
            tmp_scor.append(scores[x])
    predicted = tmp_pred[:res_cutoff]
    scores = tmp_scor[:res_cutoff]
    
    # Animate score per sentence
    animate = 0.0
    inanimate = 0.0
    
    for i in range(len(predicted)):
        if predicted[i] == 1:
            if weighted:
                animate += scores[i] # WEIGHTED
            else:
                animate += 1.0 # NOT WEIGHTED
        if predicted[i] == 0:
            if weighted:
                inanimate += scores[i] # WEIGHTED
            else:
                inanimate += 1.0 # NOT WEIGHTED
            
    if inanimate == 0.0 and animate == 0.0:
        animacy_score = 0.0
    else:
        animacy_score = animate / (animate + inanimate)    
        
    return  animacy_score


def results(y_true,y_pred,threshold):
    
    y_pred_threshold = [1 if x > threshold else 0 for x in y_pred]
    
    # Macro precision, recall, and f-score:
    precision = precision_score(y_true, y_pred_threshold, labels=[0,1], average='macro', zero_division=0)
    recall = recall_score(y_true, y_pred_threshold, labels=[0,1], average='macro', zero_division=0)
    
    fscore = 0.0
    if precision == 0 and recall == 0:
        fscore = 0.0
    else:
        fscore = (2.0 * precision * recall) / (precision + recall)

    # Micro precision, recall, and f-score:
    micro_precision = precision_score(y_true, y_pred_threshold, labels=[0,1], average='micro', zero_division=0)
    micro_recall = recall_score(y_true, y_pred_threshold, labels=[0,1], average='micro', zero_division=0)

    micro_fscore = 0.0
    if micro_precision == 0 and micro_recall == 0:
        micro_fscore = 0.0
    else:
        micro_fscore = (2.0 * micro_precision * micro_recall) / (micro_precision + micro_recall)

    rank = [[y_true[x],y_pred[x]] for x in range(len(y_pred))]

    rank.sort(key=lambda x: x[1],reverse=True)

    map_ = 0
    correct =0

    for x in range(len(rank)):
        g = rank[x][0]
        if g == 1:
            correct += 1
            map_ += correct/(x+1)
    final_map = map_/correct

    return precision, recall, fscore, micro_fscore,final_map