#https://github.com/ExcelsiorCJH/Hands-On-ML/blob/master/Chap03-Classification/Chap03-Classification.ipynb

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve,precision_recall_curve
from sklearn.model_selection import cross_val_score,cross_val_predict


def print_result_summary_of_classification(yreal,ypred):
    pass


class ClassificationBestScoreValidator():
    def __init__(self,yreal,yscore,figsize:tuple=(8,6)):
        self.yreal = yreal
        self.ypred = yscore
        self.precisions, self.recalls, self.thresholds = precision_recall_curve(yreal, yscore)
        self.fpr, self.tpr, self.thresholds = roc_curve(yreal, yscore)
        self.figsize = figsize

    def plot_precision_recall_vs_threshold(self):
        xlim_min, xlim_max = np.min(self.thresholds), np.max(self.thresholds)    
        plt.figure(figsize=self.figsize)
        plt.title('Precision_Recall vs Thresholds')
        plt.plot(self.thresholds, self.precisions[:-1], "b--", label="precision", linewidth=2)
        plt.plot(self.thresholds, self.recalls[:-1], "g-", label="recall", linewidth=2)
        plt.xlabel("thresholds", fontsize=16)
        plt.legend(loc="upper left", fontsize=16)
        plt.ylim([0, 1])
        plt.xlim([xlim_min, xlim_max])
        
        
    def plot_precision_vs_recall(self):
        
        plt.title('Precision vs Recall')
        plt.plot(self.recalls, self.precisions, "b-", linewidth=2)
        plt.xlabel("precision", fontsize=16)
        plt.ylabel("recall", fontsize=16)
        plt.axis([0, 1, 0, 1])

    def plot_roc_curve(self,label=None):
        plt.figure(figsize=self.figsize)    
        plt.plot(self.fpr, self.tpr, linewidth=2, label=label)
        plt.plot([0, 1], [0, 1], 'k--')
        plt.axis([0, 1, 0, 1])
        plt.xlabel('FPR', fontsize=16)
        plt.ylabel('TPR', fontsize=16)        
        
        


#test set
import os
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import SGDClassifier
        
        
iris = datasets.load_iris()
x = iris.data
y = iris.target
y = np.where(y==0,0,1)


sgd_clf = SGDClassifier(max_iter=5, random_state=42)
sgd_clf.fit(x, y)
y_train_pred = cross_val_predict(sgd_clf, x, y, cv=3)
y_train_pred
y_scores = cross_val_predict(sgd_clf, x, y, cv=3,
                             method="decision_function")
ys = sgd_clf.decision_function(x)
y_train_pred.shape
y_scores.shape
np.unique(y)
type(ys)
ys.shape
precision_recall_curve(y,y_scores)

v = ClassificationBestScoreValidator(y,y_scores)
v.thresholds
v.plot_precision_recall_vs_threshold()
plt.show()
v.plot_precision_vs_recall()
plt.show()