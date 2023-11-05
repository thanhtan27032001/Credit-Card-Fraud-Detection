from sklearn.model_selection import StratifiedKFold
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score


def train(x_train, y_train):
    kf = StratifiedKFold(n_splits=5, shuffle=False)
    rf = RandomForestClassifier(n_estimators=100, random_state=13)

    score = cross_val_score(rf, x_train, y_train, cv=kf, scoring='recall')
    print("Cross Validation Recall scores are: {}".format(score))
    print("Average Cross Validation Recall score: {}".format(score.mean()))


if __name__ == '__main__':
    print('All done')
