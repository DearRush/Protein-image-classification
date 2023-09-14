import torch.nn as nn
import torch.nn.functional as F


class CNN(nn.Module):
    def __init__(self):
        super(CNN,self).__init__()
        self.conv1=nn.Conv2d(3,64,padding=1,kernel_size=3)
        self.norm1=nn.BatchNorm2d(64)
        self.conv2=nn.Conv2d(64,64,padding=1,kernel_size=3)
        self.norm2=nn.BatchNorm2d(64)
        self.pool1=nn.MaxPool2d(2)
        self.norm3=nn.BatchNorm2d(64)
        self.conv3=nn.Conv2d(64,128,kernel_size=3,padding=1)
        self.norm4=nn.BatchNorm2d(128)
        self.conv4=nn.Conv2d(128,128,kernel_size=3,padding=1)
        self.norm5=nn.BatchNorm2d(128)
        self.pool2=nn.MaxPool2d(2)
        self.norm6=nn.BatchNorm2d(128)
        self.conv5=nn.Conv2d(128,256,padding=1,kernel_size=3)
        self.norm7=nn.BatchNorm2d(256)
        self.conv6=nn.Conv2d(256,256,kernel_size=3,padding=1)
        self.norm8=nn.BatchNorm2d(256)
        self.conv7=nn.Conv2d(256,256,kernel_size=3,padding=1)
        self.norm9=nn.BatchNorm2d(256)
        self.conv8=nn.Conv2d(256,256,kernel_size=3,padding=1)
        self.norm10=nn.BatchNorm2d(256)
        self.pool3=nn.MaxPool2d(2)
        self.fc1=nn.Linear(16384,512)
        self.norm11=nn.BatchNorm1d(512)
        self.drop1=nn.Dropout()
        self.fc2=nn.Linear(512,512)
        self.norm12=nn.BatchNorm1d(512)
        self.drop2=nn.Dropout()
        self.fc3=nn.Linear(512,12)
    def foward(self,x):
        x=self.norm1(F.relu(self.conv1(x)))
        x=self.norm2(F.relu(self.conv2(x)))
        x=self.norm3(self.pool1(x))
        x=self.norm4(F.relu(self.conv3(x)))
        x=self.norm5(F.relu(self.conv4(x)))
        x=self.norm6(self.pool2(x))
        x=self.norm7(F.relu(self.conv5(x)))
        x=self.norm8(F.relu(self.conv6(x)))
        x=self.norm9(F.relu(self.conv7(x)))
        x=self.norm10(F.relu(self.conv8(x)))
        x=self.pool3(x)
        x=x.view(-1,16384)
        x=self.norm11(self.fc1(x))
        x=self.drop1(x)
        x=x.view(-1,512)
        x=self.norm12(self.fc2(x))
        x=self.drop2(x)
        x=x.view(-1,512)
        x=self.fc3(x)
        x=x.view(-1,12)
        x=F.softmax(x,dim=1)
        return x


