from sklearn.metrics import confusion_matrix,precision_score,recall_score

def evaluate(y_true,y_pred):

    cm = confusion_matrix(y_true,y_pred)

    precision = precision_score(y_true,y_pred)

    recall = recall_score(y_true,y_pred)

    return cm,precision,recall