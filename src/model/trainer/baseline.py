from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, roc_auc_score, f1_score, confusion_matrix


class Trainer():
    def __init__(self, x_train, y_train, x_test, y_test,
                 lowercase=False, tokenize=None, preprocessor=None) -> None:
        self.x_train = x_train
        self.y_train = y_train
        self.x_test = x_test
        self.y_test = y_test
        self.vectorizer = CountVectorizer(lowercase=lowercase,
                                          tokenizer=tokenize,
                                          preprocessor=preprocessor)

    def train(self):
        x_train_vec = self.vectorizer.fit_transform(self.x_train)
        # Positiveが極端に少ない不均衡データセットなので重みをつける。 TODO: ちゃんと計算する
        weights = {
            0: 1 / 287,
            1: 1 / 16,
        }
        self.model = LogisticRegression(solver='liblinear', class_weight=weights)
        self.model.fit(x_train_vec, self.y_train)
        return self.model

    def predict(self, x, proba=True):
        x_vec = self.vectorizer.transform(x)
        if proba:
            predictor = self.model.predict_proba
        else:
            predictor = self.model.predict
        return predictor(x_vec)

    def eval_and_print(self):
        y_pred = self.predict(self.x_test, proba=False)
        print('accuracy_score', accuracy_score(self.y_test, y_pred))
        print('precision_score', precision_score(self.y_test, y_pred))
        print('recall_score', recall_score(self.y_test, y_pred))
        print('roc_auc_score', roc_auc_score(self.y_test, y_pred))
        print('f1_score', f1_score(self.y_test, y_pred))
        tn, fp, fn, tp = confusion_matrix(self.y_test, y_pred).ravel()
        print('tn, fp, fn, tp', tn, fp, fn, tp)
