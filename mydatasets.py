import PIL.Image
from torch.utils.data.dataset import Dataset
import torchvision.transforms as transform
from PIL import Image
import cv2
import os
import numpy as np

class CreateDatasets(Dataset):
    def __init__(self, ori_imglist,img_size):
        self.ori_imglist = ori_imglist
        self.transform = transform.Compose([
            transform.ToTensor(),
            transform.Resize((img_size, img_size)),
            transform.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
        ])

    def __len__(self):
        return len(self.ori_imglist)

    def __getitem__(self, item):

        real_img = cv2.imread(self.ori_imglist[item])#.replace('.png', '.jpg'))
        label_img = cv2.imread(self.ori_imglist[item].replace('train','label').replace('.jpg', '.jpg'))
        label_img=self.transform(label_img)
        real_img = self.transform(real_img)
        return  real_img,label_img