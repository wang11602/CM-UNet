import random
import glob


def split_data(dir_root):
    random.seed(0)
    ori_img = glob.glob(dir_root + '/*.jpg')
    k = 0.1
    train_ori_imglist = []
    val_ori_imglist = []
    sample_data = random.sample(population=ori_img, k=int(k * len(ori_img)))
    for img in ori_img:
        if img in sample_data:
            val_ori_imglist.append(img)
        else:
            train_ori_imglist.append(img)
    return train_ori_imglist, val_ori_imglist


if __name__ == '__main__':
    a, b= split_data('../base')
