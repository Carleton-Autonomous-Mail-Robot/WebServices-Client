import pickle

class Configuration:

    def __init__(self):
        pass

    def __load_pickle(self):
        with open('config.pkl','rb') as f:
            return pickle.load(f)

    def __save_pickle(self):
        with open('config.pkl','wb') as f:
            pickle.dump(self)

    def getLocation(self):
        pass
    def getClientID(self):
        pass
    def __saveConfig(self):
        pass


