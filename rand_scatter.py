def scatter():
    from matplotlib import pyplot as plt
    import numpy as np
    X = np.random.rand(100, 1)
    Y = np.random.rand(100, 1)
    fig, ax = plt.subplots(1, 3)
    ax[0].hist(X)
    ax[0].title('X')
    ax[1].hist(Y)
    ax[1].title('Y')
    ax[2].scatter(X, Y)
    ax[2].title('X Vs. Y')
    plt.show()

