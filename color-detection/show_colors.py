import cv2
import numpy as np
import argparse
import ntpath
from os import walk
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import csv

def find_histogram(clt):
    """
    create a histogram with k clusters
    :param: clt
    :return:hist
    """
    numLabels = np.arange(0, len(np.unique(clt.labels_)) + 1)
    (hist, _) = np.histogram(clt.labels_, bins=numLabels)

    hist = hist.astype("float")
    hist /= hist.sum()
    return hist

def plot_colors(hist, centroids):
    bar = np.zeros((50, 300, 3), dtype="uint8")
    startX = 0

    for (percent, color) in zip(hist, centroids):
        print("Color %s" %color.astype("uint8").tolist())
        print("Percentage %d%%" %int(percent*100))
        # plot the relative percentage of each cluster
        endX = startX + (percent * 300)
        cv2.rectangle(bar, (int(startX), 0), (int(endX), 50),
                      color.astype("uint8").tolist(), -1)
        startX = endX

    # return the bar chart
    return bar

def print_colors(hist, centroids):
    for (percent, color) in zip(hist, centroids):
        p = int(percent*100)    
        print("%d%% Color %s" %(p, color))    

def save_color_bar(bar, filename):
    head, tail = ntpath.split(filename)
    parts = tail.split(".")
    output = "{}/{}-colorbar.jpg".format(head, parts[0])
    print("Color bar stored in %s" %output)
    cv2.imwrite(output, bar)


# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-p", "--path", required=True, help="path to images")
args = vars(ap.parse_args())

with open('team_color.csv', mode='w') as team_color_file:
    team_color_writer = csv.writer(team_color_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    team_color_writer.writerow(['team', 'red', 'green', 'blue', 'percentage'])

    f = []
    for (dirpath, dirnames, filenames) in walk(args["path"]):
        print(filenames)
        for filename in filenames:
            image_file = args["path"] + "/" + filename
            print(image_file)
            img = cv2.imread(image_file)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            img = img.reshape((img.shape[0] * img.shape[1],3)) #represent as row*column,channel number
            clt = KMeans(n_clusters=3) #cluster number
            clt.fit(img)

            hist = find_histogram(clt)
            print_colors(hist, clt.cluster_centers_)

            bar = plot_colors(hist, clt.cluster_centers_)        

            for (percent, color) in zip(hist, clt.cluster_centers_):
                colorList = color.astype("uint8").tolist()
                # hexColor = '#%02x%02x%02x' %(colorList[0], colorList[1], colorList[2])
                team_color_writer.writerow([filename, colorList[0], colorList[1], colorList[2], int(percent*100)])

            # save_color_bar(bar, image_file)
            

# plt.axis("off")
# plt.imshow(bar)
# plt.show()

