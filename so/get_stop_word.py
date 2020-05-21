from sklearn import  datasets
from sklearn.cluster import KMeans

from sklearn.cluster import AgglomerativeClustering

x,y=datasets.make_moons(n_samples=400,shuffle=True,noise=0.2,random_state=None)
import  matplotlib.pyplot as plt
plt.scatter(x=range(len(x)))
md_pred=AgglomerativeClustering(linkage='average',
                                n_clusters=4,
                                affinity='cosine'
                                ).fit_predict(co_mat)