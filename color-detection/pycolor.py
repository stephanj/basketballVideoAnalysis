# -*- coding: utf-8 -*-
import random
import numpy as np
import cv2
import numpy.ma as ma
from sklearn.cluster import KMeans, SpectralClustering
from colormap import rgb2hex
from multiprocessing import Pool, cpu_count
import matplotlib.pyplot as plt
import ntpath

random.seed(0)

'__author__' == "sharmaparth17@gmail.com"
'__author2__' == "sja@devoxx.com"

class ColorDetect:

    def __init__(self, img, fileName):

        self.img = img
        self.fileName = fileName        

    def best_Clust(self, img, clusters):
        clt = KMeans(n_clusters=clusters, random_state=2, n_jobs=1)
        clt.fit(img)

        return ([clusters, clt.inertia_])

    def centroid_histogram(self, clt):
        # grab the number of different clusters and create a histogram
        # based on the number of pixels assigned to each cluster
        numLabels = np.arange(0, len(np.unique(clt.labels_)) + 1)
        (hist, _) = np.histogram(clt.labels_, bins=numLabels)
        # normalize the histogram, such that it sums to one
        hist = hist.astype("float")
        hist /= hist.sum()

        return hist

    def plot_colors(self, hist, centroids):
        # initialize the bar chart representing the relative frequency
        # of each of the colors
        bar = np.zeros((50, 300, 3), dtype="uint8")
        startX = 0

        # loop over the percentage of each cluster and the color of
        # each cluster
        for (percent, color) in zip(hist, centroids):
            # plot the relative percentage of each cluster
                if color[0] > 1 and color[1] > 1 and color[2] > 1:
                    endX = startX + (percent * 2500)
                    cv2.rectangle(bar, (int(startX), 0), (int(endX), 50),
                                  color.astype("uint8").tolist(), -1)
                    startX = endX

        # return the bar chart
        return bar

    def detect_color(self):
        actualhexcod_csv = []
        colors = []
        img_reshaped = self.img.reshape(
                            (self.img.shape[0] * self.img.shape[1], 3))
        img_final = ma.masked_where(img_reshaped == [0, 0, 0], img_reshaped)

        pool = Pool(processes=cpu_count())
        results = [pool.apply_async(self.best_Clust, (img_final, w)) for w in
                   range(3, 6)]

        cluster_errors = [p.get() for p in results]
        dic = dict()
        for i in cluster_errors:
            dic[i[1]] = i[0]
        bestCluster = dic[min(dic.keys())]
        pool.close()
        pool.join()

        clt = KMeans(n_clusters=bestCluster, random_state=2, n_jobs=-1)
        clt.fit(img_final)
        hist = self.centroid_histogram(clt)
        bar = self.plot_colors(hist, clt.cluster_centers_)
    # plt.figure()
    # plt.axis("off")
    # plt.imshow(bar)
        head, tail = ntpath.split(self.fileName)
        parts = tail.split(".")
        cv2.imwrite("{}/{}-colorbar.jpg".format(head, parts[0]), bar)

#        plt.show()
        for (percent, color) in zip(hist, clt.cluster_centers_):
            requested_colour = color
            if int(requested_colour[0]) > 0 and int(
                    requested_colour[1]) > 0 and int(
                requested_colour[2]) > 0:
                hexcod = rgb2hex(int(requested_colour[0]), \
                                 int(requested_colour[1]), \
                                 int(requested_colour[2]))
                actualhexcod_csv.append(hexcod)
                colors.append({hexcod, round(percent * 100, 2)})

        return colors

