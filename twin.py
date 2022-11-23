from mpmath import *


class Twin(object):
    def __init__(self, X_l, X):
        # I1 and I2 must be a single intervals. If it have property "len", there are not single intervals
        if hasattr(X_l, 'len') or hasattr(X, 'len'):
            print("I1 or I2 is not single intervals. Check your data.")
            exit()

        if isnan(float(X.a)) or isnan(float(X.b)):
            print("The outer interval cannot be empty.")
            exit()

        self.X_l = X_l

        if (isnan(float(X_l.a)) or isnan(float(X_l.b))) and X.a == X.b:
            self.X_l = X

        self.X = X

        if isnan(self.X_l.a):
            self.X_l_width = -1
        else:
            self.X_l_width = self.X_l.wid

        self.X_width = self.X.wid

    def __str__(self):
        return "[" + str(self.X_l) + ", " + str(self.X) + "]"
