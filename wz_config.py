lr = 1e-4
epochs =100
batch = 8

betas = (0.5, 0.999)
weight_decay = 1e-5
factor = 0.1
patience = 10

data_path="/home/u2308283094/wangyu/pix2pix/data4/train"
img_size =128

# Saving checkpoints:
HMODEL_PATH = '/home/u2308283094/wangyu/pix2pix/wz/checkpoint'
HMODEL_PATH_100 = '/home/u2308283094/wangyu/pix2pix/wz/100_checkpoint'

# load_checkpoint
is_load=False
Hload='/home/u2308283094/wangyu/pix2pix/wz/100_checkpoint/Hmodel.pth'

# Saving log
log_path='/home/u2308283094/wangyu/pix2pix/wz/logging/train_logg.txt'

# tensorboard
t_log='/home/u2308283094/wangyu/pix2pix/wz/tf-logs'

