import matplotlib.pyplot as plot
import pandas as pandas
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.metrics import roc_auc_score
from sklearn.metrics import roc_curve

tabs_data = pandas.read_csv('test_tabs_data.csv')
X = tabs_data.iloc[:, [1]].values
y = tabs_data.iloc[:, 0].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

classifier = LogisticRegression(random_state=0)
classifier.fit(X_train, y_train)

y_prediction = classifier.predict(X_test)

tabs_confusion_matrix = confusion_matrix(y_test, y_prediction)
print(tabs_confusion_matrix)

logit_roc_auc = roc_auc_score(y_test, classifier.predict(X_test))
fpr, tpr, thresholds = roc_curve(y_test, classifier.predict_proba(X_test)[:,1])
plot.figure()
plot.plot(fpr, tpr, label='Logistic Regression (area = %0.2f)' % logit_roc_auc)
plot.plot([0, 1], [0, 1],'r--')
plot.xlim([0.0, 1.0])
plot.ylim([0.0, 1.05])
plot.xlabel('False Positive Rate')
plot.ylabel('True Positive Rate')
plot.title('Receiver operating characteristic')
plot.legend(loc="lower right")
plot.savefig('Log_ROC')
plot.show()
