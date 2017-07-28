import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import graphviz
from sklearn.tree import export_graphviz

def plot_decision_tree(clf, feature_names, class_names):
    export_graphviz(clf, out_file="tmp_plt.dot", feature_names=feature_names, class_names=class_names, filled = True, impurity = False)
    with open("tmp_plt.dot") as f:
        dot_graph = f.read()
    return graphviz.Source(dot_graph)

def plot_feature_importances(clf, feature_names, max_features=10):
    sort_indices = np.argsort(clf.feature_importances_)[:-(max_features+1):-1]
    
    feature_names = feature_names[sort_indices]
    feature_importances = clf.feature_importances_[sort_indices]
    
    c_features = len(feature_names)
    
    plt.barh(range(c_features), feature_importances)
    plt.xlabel("Feature importance")
    plt.ylabel("Feature name")
    plt.yticks(np.arange(c_features), feature_names)
