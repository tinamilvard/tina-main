import my_pickle

with open('data.pickle', 'rb') as f:
    data = pickle.load(f)
print(data)