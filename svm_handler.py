from sklearn import svm
from calc_error_pct import *
from parse_data import parse_data
import datetime
import cPickle

__author__ = 'stas'


class SVMHandler:
    """ In this class you will implement the classifier and it's methods. """

    def __init__(self):
        """
        initializing the class, error_percentage=-1 means it still wasnt tested and calculated.
        Checking if the classifier was saved into disk, loading it,setting a boolean to know if it
        it exists or not
        """
        self.training_path_str = "data/adult.data"
        self.test_path_str = "data/adult.test"
        self.my_saved_classifier_str = "my_saved_classifier.pkl"
        self.error_percentage = -1
        temp_clf = self.load_classifier()

        if temp_clf:
            self.classifier_exists = True
            self.classifier = temp_clf

        else:
            self.classifier_exists = False
            self.classifier = svm.SVC()

    def train(self):
        """
        training the SVM, saving the trained SVM into the local disk, this will helpful for the user
        because he can avoid running the training on the same data every time he reopens the program
        """
        print "Training Started at {0}".format(str(datetime.datetime.now()))
        x, y = parse_data(self.training_path_str)
        print "Training parse Finished at {0}".format(str(datetime.datetime.now()))
        self.classifier.fit(x, y)
        self.save_classifier(self.classifier)
        print "Training Finished at {0}".format(str(datetime.datetime.now()))

    def test(self):
        print "Test Started at {0}".format(str(datetime.datetime.now()))
        x, y = parse_data(self.test_path_str)
        print "Test parse Finished at {0}".format(str(datetime.datetime.now()))
        results_list = self.classifier.predict(x)
        self.error_percentage = calculate_error_percentage(y, results_list)
        print "Test Finished at {0}".format(str(datetime.datetime.now()))
        print "The error percentage is {0}".format(self.error_percentage)

    def is_classifier_exists(self):
        return self.classifier_exists

    def save_classifier(self, classifier):
        """save the classifier to the disk, so the learned SVM can be reused when the user 
        reopens the program"""
        with open(self.my_saved_classifier_str, 'wb') as fid:
            cPickle.dump(classifier, fid)
        self.classifier_exists = True

    def load_classifier(self):
        """load the classifier from disk: when the user reopens the program and the class is initialized,
        there will be a check if there already exists a learned SVM"""
        try:
            with open(self.my_saved_classifier_str, 'rb') as fid:
                return cPickle.load(fid)
        except Exception as e:
            print e
            return None
