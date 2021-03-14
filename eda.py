import pandas as pd
import numpy as np
from pandas_profiling import ProfileReport

train = pd.read_csv("data/train.csv")
test = pd.read_csv("data/test.csv")
store = pd.read_csv("data/store.csv")

train_pr = ProfileReport(train)
test_pr = ProfileReport(test)
store_pr = ProfileReport(store)

train_pr.to_file("train.html")
test_pr.to_file("test.html")
store_pr.to_file("store.html")