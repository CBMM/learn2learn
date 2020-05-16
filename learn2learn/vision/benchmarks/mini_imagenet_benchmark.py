#!/usr/bin/env python3

import learn2learn as l2l
from learn2learn.data.transforms import NWays, KShots, LoadData, RemapLabels, ConsecutiveLabels


def mini_imagenet_tasksets(
    train_ways=5,
    train_samples=10,
    test_ways=5,
    test_samples=10,
    root='~/data',
    **kwargs,
):
    """Tasksets for mini-ImageNet benchmarks."""
    train_dataset = l2l.vision.datasets.MiniImagenet(root=root, mode='train')
    valid_dataset = l2l.vision.datasets.MiniImagenet(root=root, mode='validation')
    test_dataset = l2l.vision.datasets.MiniImagenet(root=root, mode='test')
    train_dataset = l2l.data.MetaDataset(train_dataset)
    valid_dataset = l2l.data.MetaDataset(valid_dataset)
    test_dataset = l2l.data.MetaDataset(test_dataset)

    train_transforms = [
        NWays(train_dataset, train_ways),
        KShots(train_dataset, train_samples),
        LoadData(train_dataset),
        RemapLabels(train_dataset),
        ConsecutiveLabels(train_dataset),
    ]
    valid_transforms = [
        NWays(valid_dataset, test_ways),
        KShots(valid_dataset, test_samples),
        LoadData(valid_dataset),
        ConsecutiveLabels(valid_dataset),
        RemapLabels(valid_dataset),
    ]
    test_transforms = [
        NWays(test_dataset, test_ways),
        KShots(test_dataset, test_samples),
        LoadData(test_dataset),
        RemapLabels(test_dataset),
        ConsecutiveLabels(test_dataset),
    ]

    _datasets = (train_dataset, valid_dataset, test_dataset)
    _transforms = (train_transforms, valid_transforms, test_transforms)
    return _datasets, _transforms