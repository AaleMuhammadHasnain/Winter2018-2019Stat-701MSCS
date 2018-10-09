import numpy as np
import matplotlib as plt
import math
import pandas as pd

def mlr_estimate(x1 ,x2 , y):

    totalObsservations = np.size(x1)
    print("Total Observations = {}".format(totalObsservations))
    k = 2
    print("Value of K = {}".format(k))
    mean_x1 ,mean_x2 , mean_y = np.mean(x1) ,np.mean(x2) , np.mean(y)
    print("Mean (X1) = {} \nMean (X2) = {}\nMean of (Y) = {}".format(np.mean(x1), np.mean(x2), np.mean(y)))

    squareOfx2 = (np.sum((x2 - mean_x2) ** 2))
    print("Sum of Square(X2) = {}".format(squareOfx2))
    sumOfSquareX1X2 = (np.sum((x1 - mean_x1) * (x2 - mean_x2)))
    print("Sum of Square of (X1X2) = {}".format(sumOfSquareX1X2))
    sumOfSquareX1Y = (np.sum((x1 - mean_x1) * (y - mean_y)))
    print("Sum of Square (X1Y) = {}".format(sumOfSquareX1Y))
    sumOfSquareX1 = (np.sum((x1 - mean_x1) ** 2))
    print("Sum of Square (X1) = {}".format(sumOfSquareX1))
    sumOfSquareX2Y = (np.sum((x2 - mean_x2) * (y - mean_y)))
    print("Sum of Square(X2Y) = {}".format(sumOfSquareX1Y))
    cal1 = (squareOfx2 * sumOfSquareX1Y)
    cal2 = (sumOfSquareX1X2 * sumOfSquareX2Y)
    cal3 = (sumOfSquareX1 * squareOfx2)
    cal4 = (sumOfSquareX1X2 * sumOfSquareX1X2)
    cal5 = (sumOfSquareX1 * sumOfSquareX2Y)
    cal6 = (sumOfSquareX1X2 * sumOfSquareX1Y)

    b1 = float(cal1 - cal2)/float(cal3 - cal4)
    b2 = float((cal5 - cal6)/float(cal3 - cal4))
    b0 = float(mean_y - b1 * mean_x1 - b2 * mean_x2)
    print("\nCo-efficient Estimation:\nb0 = {}  \nb1 = {} \nb2 = {}".format(b0, b1, b2))
    tss = np.sum((y - mean_y) ** 2)
    print("\nTSS = {} ".format(tss))
    y_hat = (b0 + (b1 * x1) + (b2 * x2))
    print("y^ = {}".format(y_hat))
    mss = (np.sum((y_hat - mean_y) ** 2))
    print("MSS/SSR = {}".format(mss))
    rss = (np.sum((y - y_hat) ** 2))
    print("RSS/SSE = {}".format(rss))
    r2 = float(mss / tss)
    print("Determination Co-efficient (R^2) = {}".format(r2))
    sum_of_y_hat = np.sum(y_hat)
    print("Sum of Y^ = {}".format(sum_of_y_hat))
    r1 = float(rss/(totalObsservations-1-k))
    print("r2 = {}".format(r1))
    vb1 = r1 * float(squareOfx2/float(cal3 - cal4))
    print("Varience (b1) = {}".format(vb1))
    vb2 = r1 * float(sumOfSquareX1/float(cal3 - cal4))
    print("Varience (b2) = {}".format(vb2))
    vb0 = r1 * float((1/totalObsservations) + float((mean_x1 * squareOfx2) + (mean_x2 * sumOfSquareX1) + (2 * mean_x1 * mean_x2 * sumOfSquareX1X2))/float(cal3 - cal4))
    print("Varience (b0) = {}".format(vb0))

def main():
    x1_array = list()
    x1_range = input("Enter the number of x1 elements you want:")
    print('Enter numbers in x1: ')
    for i in range(int(x1_range)):
       n1 = input()
       x1_array.append(float(n1))
    x2_array = list()

    print('Enter numbers in x2: ')
    for i in range(int(x1_range)):
       n2 = input()
       x2_array.append(float(n2))
    y_array = list()

    print('Enter numbers in y: ')
    for i in range(int(x1_range)):
       n3 = input()
       y_array.append(float(n3))

    mlr_estimate(x1_array ,x2_array ,y_array)
main()
