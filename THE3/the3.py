from math import exp


def relu(lst):
    return [max(i, 0) for i in lst]


def sigmoid(lst):
    a = []
    for i in range(len(lst)):
        if lst[i] <= -700:
            a.append(0)
        elif -700 < lst[i] < 700:
            a.append(1 / (1 + exp(-lst[i])))
        elif 700 <= lst[i]:
            a.append(1)
    return a


def linear(X, Weights):
    b = []
    for j in range(len(Weights)):
        a = 0
        for i in range(len(X)):
            a = a + X[i] * Weights[j][i]
        b.append(a)
    return b


def forward_pass(Network, X):

    for i in range(len(Network)):
        if Network[i][:4] == "relu":
            X = relu(X)

        elif Network[i][:7] == "sigmoid":
            X = sigmoid(X)

        elif Network[i][0][:6] == "linear":
            X = linear(X, Network[i][1])

    return X