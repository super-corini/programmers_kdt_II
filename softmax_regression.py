import numpy as np
from sklearn.datasets import make_classification
from sklearn.datasets import fetch_openml

mnist = fetch_openml('mnist_784')
mnist.keys()

X, y = mnist["data"], mnist["target"]

y = y.astype(np.uint8)

from sklearn.preprocessing import OneHotEncoder
enc = OneHotEncoder()

enc.fit(y[:,np.newaxis])

Y = enc.transform(y[:,np.newaxis]).toarray()

X_train, X_test, y_train, y_test = X[:60000], X[60000:], Y[:60000], Y[60000:]

X_train = X_train / 255
X_test = X_test / 255

def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def softmax(X, W):
    K = np.size(W, 1)
    A = np.exp(X @ W)
    B = np.diag(1 / (np.reshape(A @ np.ones((K,1)), -1)))
    Y = B @ A
    return Y

def compute_cost(X, T, W, lambda_):
    epsilon = 1e-5
    N = len(T)
    K = np.size(T, 1)
    cost = - (1/N) * np.ones((1,N)) @ (np.multiply(np.log(softmax(X, W) + epsilon), T)) @ np.ones((K,1)) + (lambda_) * (np.linalg.norm(W, ord=2) ** 2)
    return cost 

def predict(X, W):
    return np.argmax((X @ W), axis=1)

def batch_gd(X, T, W, learning_rate, iterations, batch_size, lambda_):
    N = len(T)
    cost_history = np.zeros((iterations,1))
    shuffled_indices = np.random.permutation(N)
    X_shuffled = X[shuffled_indices]
    T_shuffled = T[shuffled_indices]

    for i in range(iterations):
        j = i % N
        X_batch = X_shuffled[j:j+batch_size]
        T_batch = T_shuffled[j:j+batch_size]
        # batch가 epoch 경계를 넘어가는 경우, 앞 부분으로 채워줌
        if X_batch.shape[0] < batch_size:
            X_batch = np.vstack((X_batch, X_shuffled[:(batch_size - X_batch.shape[0])]))
            T_batch = np.vstack((T_batch, T_shuffled[:(batch_size - T_batch.shape[0])]))
        W = W - (learning_rate/batch_size) * (X_batch.T @ (softmax(X_batch, W) - T_batch) + 2*(lambda_)*W)
        cost_history[i] = compute_cost(X_batch, T_batch, W, lambda_)
        if i % 1000 == 0:
            print(cost_history[i][0])

    return (cost_history, W)

best_score = 0
best_lambda = 0
for lambda_ in range(10):
    lambda_ = float(lambda_ / 100.0)
    print(lambda_)
    X = np.hstack((np.ones((np.size(X_train, 0),1)),X_train))
    T = y_train

    K = np.size(T, 1)
    M = np.size(X, 1)
    W = np.zeros((M,K))

    iterations = 50000
    learning_rate = 0.01

    initial_cost = compute_cost(X, T, W, lambda_)

    print("Initial Cost is: {} \n".format(initial_cost[0][0]))

    (cost_history, W_optimal) = batch_gd(X, T, W, learning_rate, iterations, 64, lambda_)

    ## Accuracy
    X_ = np.hstack((np.ones((np.size(X_test, 0),1)),X_test))
    T_ = y_test
    y_pred = predict(X_, W_optimal)
    score = float(sum(y_pred == np.argmax(T_, axis=1)))/ float(len(y_test))
    print(score)
    if score > best_score:
        best_score = score
        best_lambda = lambda_

print('best_score : {}'.format(best_score))
print('best_lambda : {}'.format(best_lambda))