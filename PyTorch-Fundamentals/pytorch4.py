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
        y_pred = self.linear(x)
        return y_pred


#initlize model
model = Model()


#Mean Square loss
criterion = torch.nn.MSELoss(size_average=False)
#here SGD stands for Standaard gradient descent  default params and learning rate
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


#convert data you want to predict also into a Variable
hour_var = Variable(torch.Tensor([[4.0]]))
#preict
y_pred = model(hour_var)
print("predict (after training)",  4, model(hour_var).data[0][0])
