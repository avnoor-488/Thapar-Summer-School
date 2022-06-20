import torch
from torch.autograd import Variable
import torch.nn.functional as F

x_data = Variable(torch.Tensor([[1.0], [2.0], [3.0]]))
y_data = Variable(torch.Tensor([[2.0], [4.0], [6.0]]))


class Model(torch.nn.Module):
	#initialize parameters model --> linear and one input and one output
	#forward function --> predict based on linear
    def __init__(self):

        super(Model, self).__init__()
        self.linear = torch.nn.Linear(1, 1)  # One in and one out

    def forward(self, x):
        y_pred = F.sigmoid(self.linear(x))
        return y_pred


#initlize model
model = Model()


#Mean Square loss
criterion = torch.nn.BCELoss(size_average=False)
#here SGD stands for Standard gradient descent  default params and learning rate
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)


#training epochs
for epoch in range(500):
    #this is like a forward pass
    y_pred = model(x_data)

    #calculate loss on predicted and actual
    loss = criterion(y_pred, y_data)
    print(epoch, loss.data[0])
    #so till now we have got the loss from the variable graph now we need to back prop and update
    #initlize
    optimizer.zero_grad()
    #back prop the loss since loss is alredy a variable 
    loss.backward()
    #Update the weightss
    optimizer.step()


hour_var = Variable(torch.Tensor([[1.0]]))
print("predict 1 hour ", 1.0, model(hour_var).data[0][0] > 0.5)
hour_var = Variable(torch.Tensor([[7.0]]))
print("predict 7 hours", 7.0, model(hour_var).data[0][0] > 0.5)
