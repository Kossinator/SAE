
from scipy.spatial.distance import euclidean
from operator import itemgetter



class KNN_Classifier():


    def normalize(self):
        columns = []
        for row in self.X:
            for _ in row:
                columns.append([])
        for row in self.X:
            for i in range(len(row)):
                columns[i].append(row[i])
        new_X = []
        for row in self.X:
            new_row = []
            for i in range(len(row)):
                new_row.append((row[i] - min(columns[i])) / (max(columns[i])-min(columns[i])))
            new_X.append(new_row)
        self.X_normalized = new_X


    def __init__(self, K):
        self.K = K
        self.X = None
        self.X_normalized = None


    def get_KNN_dominant_class(self, item):
        distances = []
        for i in range(len(self.X)):
            dist = euclidean(item, self.X_normalized[i])
            distances.append([dist, self.y[i]])
        distances = sorted(distances, key=itemgetter(0), reverse=False)
        distances = distances[:self.K]
        diff_classes = []
        for d in distances:
            if not d[1] in diff_classes:
                diff_classes.append(d[1])
        counter_array = []
        counter = 0
        for i in range(len(diff_classes)):
            for d in distances:
                if diff_classes[i] == d[1]:
                    counter += 1
            counter_array.append(counter)
            counter = 0
        max_index = counter_array.index(max(counter_array))
        return diff_classes[max_index]


    def fit(self, X, y):
        self.X = X
        self.y = y
        self.normalize()


    def normalize_prediction_item(self, item):
        columns = []
        for row in self.X:
            for _ in row:
                columns.append([])
        for row in self.X:
            for i in range(len(row)):
                columns[i].append(row[i])
        new_item = []
        for i in range(len(item)):
            new_item.append((item[i] - min(columns[i])) / (max(columns[i])-min(columns[i])))
        return new_item


    def predict(self, list_to_predict):
        predictions = []
        for item in list_to_predict:
            item = self.normalize_prediction_item(item)
            predictions.append(self.get_KNN_dominant_class(item))
        return predictions



