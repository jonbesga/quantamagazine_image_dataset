import datasets

dataset = datasets.load_dataset("imagefolder", data_dir="./dataset")
dataset.push_to_hub("jonbesga/quantamagazine")