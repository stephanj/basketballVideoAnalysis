import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plotClusters(self):
    #plotting 
    fig = plt.figure()
    ax = Axes3D(fig)        
    for label, pix in zip(self.LABELS, self.IMAGE):
        ax.scatter(pix[0], pix[1], pix[2], color = self.rgb_to_hex(self.COLORS[label]))
    plt.show()

csvfile = "team_color.csv"
data = pd.read_csv(csvfile)
plotClusters(data)

# sns.pairplot(data, hue="team")
# plt.show()

