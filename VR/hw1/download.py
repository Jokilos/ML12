import torchvision

# Directory for dataset storage
DATA_PATH = "~/torch_datasets/voc"

TRAIN_DATASET = torchvision.datasets.VOCSegmentation(
    root=DATA_PATH,
    year="2011",
    image_set="train",
    download=True,
    transform=None,
    target_transform=None,
)

TEST_DATASET = torchvision.datasets.VOCSegmentation(
    root=DATA_PATH,
    year="2011",
    image_set="val",
    download=True,
    transform=None,
    target_transform=None,
)