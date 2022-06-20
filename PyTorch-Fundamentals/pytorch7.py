#over a period of time as data gets bigger and bigger
# we should divide the data into batches as a performance enhancer
# we go one batch at a time calculate the gradient and update 

# 1000 training examples 
# batch size 500
# so it will take 2 iterations to complete 1 epoch

# so DATALOADER in pytorch will handle this issue for us
import torch
import numpy as np
from torch.autograd import Variable
from torch.utils.data import Dataset, DataLoader


class DiabetesDataset(Dataset):

    def __init__(self):
        xy = np.loadtxt('diabetes.csv',
                        delimiter=',', dtype=np.float32)
        self.len = xy.shape[0]
        self.x_data = torch.from_numpy(xy[:, 0:-1])
        self.y_data = torch.from_numpy(xy[:, [-1]])

    def __getitem__(self, index):
        return self.x_data[index], self.y_data[index]

    def __len__(self):
        return self.len


dataset = DiabetesDataset()
train_loader = DataLoader(dataset=dataset,
                          batch_size=32,
                          shuffle=True,
                          num_workers=2)

for epoch in range(2):
    for i, data in enumerate(train_loader, 0):
        
        inputs, labels = data
        inputs, labels = Variable(inputs), Variable(labels)
        print(epoch, i, "inputs", inputs.data, "labels", labels.data)
