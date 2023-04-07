import matplotlib.pyplot as plt


def plot_Graph(y,X,X_test,y_pred,y_test,title):
    fig, (ax1, ax2) = plt.subplots(1, 2)
    fig.suptitle(title)
    ax1.plot(y,X)
    ax2.plot(y_test,X_test,c='blue',linestyle='dotted')
    ax2.plot(y_pred,X_test,c='red',linestyle='dashed') 
    plt.show(block=False)