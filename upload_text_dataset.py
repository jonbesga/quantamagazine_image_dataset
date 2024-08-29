import datasets

dataset = datasets.load_dataset("text", data_files={"train": ["image_links.txt"]})
dataset.push_to_hub("jonbesga/quantamagazine")