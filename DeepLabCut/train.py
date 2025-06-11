# train.py

import deeplabcut

def train_model(config_path, shuffle=1, max_iters=10000):
    deeplabcut.create_training_dataset(config_path, net_type='resnet_50', Shuffles=[shuffle])
    deeplabcut.train_network(config_path, shuffle=shuffle, displayiters=10, saveiters=500, maxiters=max_iters)
    deeplabcut.export_model(config_path, shuffle=shuffle, trainingsetindex=0)

def evaluate_model(config_path, plotting=True):
    deeplabcut.evaluate_network(config_path, plotting=plotting)
