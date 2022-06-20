import numpy as np
import matplotlib.pyplot as plt

x_data = [1.0, 2.0, 3.0]
y_data = [2.0, 4.0, 6.0]

w=1.0
#like we have that y=ax+b we can treak here aisa ki x*w
def forward(x):
    return x * w


# Square loss the one we used in yolo!
def loss(x, y):
    y_pred = forward(x)
    return (y_pred - y) * (y_pred - y)


def gradient(x,y):

    return 2*x*(x*w-y)




# ikkada weights update cheyakunda try chesamu
print("Before update",  4, forward(4))

# here we did update weights 
for epoch in range(10):
    for x_val, y_val in zip(x_data, y_data):
        grad = gradient(x_val, y_val)
        w = w - 0.01 * grad#ikkaga 0.01 is the learning rate gurthu petukovalisndi enti ante smaller the learning rate greater the accuracy
        #kani smaller the learning rate more the time it will take to learn, anduvaluna una computation power batti nerchukovali
        print("\tgrad: ", x_val, y_val, round(grad, 2))
        l = loss(x_val, y_val)

    print("progress:", epoch, "w=", round(w, 2), "loss=", round(l, 2))

# update taruvata chudamu emi avutundo
print("after update in other words training",  "4 hours", forward(4))