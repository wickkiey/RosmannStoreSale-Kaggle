import pandas as pd
import numpy as np


train = pd.read_csv("data/train.csv")
test = pd.read_csv("data/test.csv")
store = pd.read_csv("data/store.csv")


print("train Shape ",train.shape)
print("test shape ",test.shape)
print("store shape", store.shape)


