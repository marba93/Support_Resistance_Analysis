import pandas as pd
import numpy as np
# import matplotlib
# import matplotlib.pyplot as plt


# input data

df = pd.read_csv(r"/Users/marcosbrionesalvarez/Downloads/Price and Support-Resistance Data Sept 2018 - Dec 2020 (Version 2).csv")
print(df)
df = df[df['Type']=='Copper']
print(df)
inputs = df['USD'].to_list()
outputs = df['Support'].to_list()
# df = df.loc[1:525, 'USD']
# inputs = df.to_numpy()

inputs = np.array([
  [7815.5],
  [7854],
  [7811.5],
  [7811.5],
  [7811.5],
  [7784.5],
  [7858.5],
  [7858.5],
  [7914],
  [7914],
  [7847.5],
  [7775.5],
  [7787],
  [7760],
  [7729.5],
  [7723.5],
  [7647.5],
  [7672],
  [7748.5],
  [7623],
  [7623],
  [7649],
  [7681],
  [7476.5],
  [7370.5],
  [7257.5],
  [7314],
  [7233.5],
  [7195],
  [7046.5],
  [7101.5],
  [7071],
  [7128.5],
  [6943.5],
  [6921.5],
  [6934],
  [6882],
  [7045],
  [6946.5],
  [6808],
  [6760],
  [6801],
  [6725],
  [6706],
  [6708],
  [6713.5],
  [6807.5],
  [6824.5],
  [6897.5],
  [6901.5],
  [6836.5],
  [6773.5],
  [6740.5],
  [6698],
  [6715.5],
  [6705.5],
  [6770.5],
  [6741],
  [6622.5],
  [6538],
  [6528],
  [6519.5],
  [6418.5],
  [6628],
  [6612],
  [6558],
  [6584.5],
  [6523],
  [6534],
  [6784],
  [6784],
  [6804.5],
  [6801],
  [6737.5],
  [6757],
  [6800.5],
  [6762],
  [6729],
  [6684.5],
  [6681],
  [6736],
  [6772],
  [6655],
  [6604],
  [6705],
  [6768],
  [6702],
  [6702],
  [6575],
  [6584],
  [6525],
  [6559.5],
  [6542],
  [6648],
  [6648],
  [6486.5],
  [6428],
  [6334],
  [6373.5],
  [6380.5],
  [6361],
  [6361.5],
  [6428.5],
  [6450.5],
  [6523],
  [6435],
  [6435],
  [6439.5],
  [6428],
  [6468],
  [6393],
  [6420],
  [6389.5],
  [6510.5],
  [6506],
  [6505],
  [6410.5],
  [6447],
  [6384],
  [6510],
  [6491],
  [6537],
  [6320],
  [6339.5],
  [6197.5],
  [6089],
  [6105],
  [6021],
  [6083],
  [6023.5],
  [6043.5],
  [5966.5],
  [5984.5],
  [5888],
  [5882.5],
  [5909],
  [5846],
  [5855],
  [5825],
  [5763],
  [5787.5],
  [5673.5],
  [5809],
  [5825],
  [5822],
  [5704],
  [5678.5],
  [5607],
  [5478.5],
  [5522],
  [5487.5],
  [5404],
  [5357],
  [5306.5],
  [5342.5],
  [5375],
  [5272],
  [5272],
  [5360.5],
  [5360.5],
  [5343.5],
  [5277.5],
  [5194.5],
  [5186.5],
  [5245],
  [5263.5],
  [5266],
  [5257],
  [5257],
  [5228],
  [5142.5],
  [5086],
  [5090.5],
  [5258.5],
  [5215],
  [5197.5],
  [5190],
  [5142],
  [5147.5],
  [5061.5],
  [5029.5],
  [5190],
  [5193.5],
  [5121.5],
  [5085.5],
  [5150],
  [4992.5],
  [4992.5],
  [4992.5],
  [5000.5],
  [5085.5],
  [4881],
  [4880.5],
  [4840.5],
  [4787],
  [4811.5],
  [4773],
  [4785.5],
  [4789.5],
  [4766.5],
  [4797.5],
  [4626.5],
  [4868],
  [4690],
  [4881],
  [5218],
  [5221],
  [5548],
  [5400],
  [5562],
  [5608.5],
  [5495],
  [5640],
  [5688],
  [5718],
  [5689],
  [5657],
  [5597],
  [5640],
  [5639.5],
  [5687],
  [5681],
  [5727],
  [5746],
  [5770],
  [5758],
  [5811],
  [5753],
  [5740],
  [5764],
  [5714],
  [5667],
  [5670],
  [5740],
  [5735],
  [5666],
  [5602],
  [5588],
  [5635],
  [5723],
  [5746],
  [5809],
  [5996],
  [6082],
  [6139],
  [6186],
  [6271],
  [6306],
  [6330],
  [6270],
  [6280],
  [6201],
  [6184],
  [6186],
  [6175],
  [6159],
  [6119.5],
  [6105],
  [6192],
  [6183],
  [6183],
  [6215],
  [6240],
  [6213],
  [6213],
  [6213],
  [6171],
  [6186],
  [6185],
  [6161],
  [6196],
  [6177],
  [6177],
  [6119],
  [6109],
  [6087],
  [6012],
  [5900],
  [5885],
  [5850],
  [5835],
  [5877],
  [5877],
  [5950],
  [5950],
  [5872],
  [5886.5],
  [5851],
  [5851],
  [5830],
  [5898],
  [5843],
  [5851],
  [5835],
  [5854],
  [5850],
  [5860],
  [5877],
  [5965.5],
  [5949],
  [5932],
  [5912],
  [5875],
  [5819],
  [5850],
  [5913],
  [5902],
  [5910],
  [5887],
  [5887],
  [5801],
  [5826],
  [5843],
  [5775],
  [5758],
  [5709],
  [5780],
  [5755],
  [5797],
  [5732],
  [5692],
  [5688],
  [5668.5],
  [5635],
  [5657],
  [5662],
  [5640],
  [5761],
  [5743],
  [5792],
  [5750],
  [5790],
  [5728],
  [5805],
  [5780],
  [5780],
  [5796],
  [5907.5],
  [5896],
  [5875],
  [5795],
  [5767],
  [5795],
  [5814],
  [5802],
  [5691],
  [5562],
  [5637],
  [5695.5],
  [5738],
  [5673.5],
  [5685.5],
  [5696.5],
  [5690.25],
  [5724],
  [5728.5],
  [5789.75],
  [5734],
  [5728],
  [5755.5],
  [5726],
  [5749],
  [5766.5],
  [5747.5],
  [5704.75],
  [5690.5],
  [5677.5],
  [5792.5],
  [5902.5],
  [5949.5],
  [5966],
  [5972],
  [5965.5],
  [6032.5],
  [6000.5],
  [5998.5],
  [6029],
  [6077.5],
  [5955.5],
  [5937],
  [5980.5],
  [5994.5],
  [5962.5],
  [5934.5],
  [5879],
  [5821.75],
  [5929],
  [5867.5],
  [5914.75],
  [5886],
  [5925.5],
  [6011.5],
  [5981],
  [5967.25],
  [6017.25],
  [6004.5],
  [5932.25],
  [5951.5],
  [5971.75],
  [5919.5],
  [5875.5],
  [5787.5],
  [5827.25],
  [5828.5],
  [5847],
  [5915.5],
  [5810.5],
  [5785.25],
  [5822.5],
  [5859.25],
  [5826.5],
  [5819.5],
  [5818],
  [5853],
  [5889],
  [5977.5],
  [5947.5],
  [5896],
  [5956],
  [6034],
  [6010.5],
  [6043.5],
  [6111.5],
  [6031.5],
  [6039.5],
  [6068],
  [6146],
  [6120.5],
  [6125.5],
  [6177.5],
  [6180.25],
  [6214.5],
  [6383.5],
  [6432.5],
  [6371],
  [6387.75],
  [6379.5],
  [6441],
  [6439],
  [6455.5],
  [6532.5],
  [6486.5],
  [6474.5],
  [6514.25],
  [6442.5],
  [6465.5],
  [6506.5],
  [6451],
  [6433],
  [6462.5],
  [6487.5],
  [6439.75],
  [6491.5],
  [6477],
  [6372.25],
  [6338.5],
  [6339],
  [6323.75],
  [6368],
  [6500.75],
  [6468],
  [6483.5],
  [6457],
  [6400.25],
  [6390.25],
  [6485.5],
  [6482.5],
  [6401],
  [6367],
  [6420.25],
  [6453.5],
  [6487.5],
  [6397.5],
  [6523.75],
  [6493.5],
  [6493.5],
  [6462.5],
  [6495.25],
  [6458],
  [6372.25],
  [6336],
  [6235.5],
  [6237.5],
  [6183.25],
  [6178.5],
  [6129.5],
  [6118.25],
  [6164.75],
  [6227.5],
  [6246.25],
  [6230],
  [6190.5],
  [6104],
  [6124],
  [6167],
  [6095.5],
  [6028],
  [6026],
  [5925.25],
  [5921.5],
  [5955.5],
  [5961.5],
  [5984],
  [6044],
  [5964.5],
  [5945.5],
  [5915.5],
  [5890.5],
  [5947.5],
  [5931.5],
  [5981],
  [5921],
  [5913],
  [5857.5],
  [5836],
  [5861.5],
  [6099.39],
  [6169.03],
  [6206.09],
  [6066.34],
  [6265.6],
  [6851.49],
  [6877.84],
  [7043.75],
  [7122.13]
])


# output data

# df2 = pd.read_csv(r"C:\Users\danie\OneDrive - Washington University in St. Louis\MetalMiner\Support-Resistance Project\Price and Support-Resistance Data (Version 3).csv")
# df2 = df2.loc[1:525, 'Support']
# outputs = df2.to_numpy()

outputs = np.array([
  [6944],
  [6944],
  [6944],
  [6944],
  [6944],
  [6944],
  [6944],
  [6944],
  [6944],
  [6944],
  [6944],
  [6944],
  [6944],
  [6944],
  [6944],
  [6944],
  [6944],
  [6944],
  [6944],
  [6944],
  [6944],
  [6944],
  [6334],
  [6334],
  [6334],
  [6334],
  [6334],
  [6334],
  [6334],
  [6334],
  [6334],
  [6334],
  [6334],
  [6334],
  [6334],
  [6334],
  [6334],
  [6334],
  [6334],
  [6334],
  [6334],
  [6334],
  [6334],
  [6334],
  [6334],
  [6334],
  [6334],
  [6334],
  [6334],
  [6334],
  [6334],
  [6334],
  [6334],
  [6334],
  [6334],
  [6334],
  [6334],
  [6334],
  [6334],
  [6334],
  [6334],
  [6334],
  [6334],
  [6334],
  [6201],
  [6201],
  [6201],
  [6201],
  [6201],
  [6201],
  [6201],
  [6201],
  [6201],
  [6201],
  [6201],
  [6201],
  [6201],
  [6201],
  [6201],
  [6201],
  [6201],
  [6201],
  [6201],
  [6201],
  [6201],
  [6201],
  [5888],
  [5888],
  [5888],
  [5888],
  [5888],
  [5888],
  [5888],
  [5888],
  [5888],
  [5888],
  [5888],
  [5888],
  [5888],
  [5888],
  [5888],
  [5888],
  [5888],
  [5888],
  [5888],
  [5888],
  [5888],
  [5548],
  [5548],
  [5548],
  [5548],
  [5548],
  [5548],
  [5548],
  [5548],
  [5548],
  [5548],
  [5548],
  [5548],
  [5548],
  [5548],
  [5548],
  [5548],
  [5548],
  [5548],
  [5548],
  [5548],
  [5548],
  [5548],
  [5548],
  [4993],
  [4993],
  [4993],
  [4993],
  [4993],
  [4993],
  [4993],
  [4993],
  [4993],
  [4993],
  [4993],
  [4993],
  [4993],
  [4993],
  [4993],
  [4993],
  [4993],
  [4993],
  [4993],
  [4993],
  [4993],
  [4993],
  [4850],
  [4850],
  [4850],
  [4850],
  [4850],
  [4850],
  [4850],
  [4850],
  [4850],
  [4850],
  [4850],
  [4850],
  [4850],
  [4850],
  [4850],
  [4850],
  [4850],
  [4850],
  [4850],
  [4850],
  [4850],
  [4627],
  [4627],
  [4627],
  [4627],
  [4627],
  [4627],
  [4627],
  [4627],
  [4627],
  [4627],
  [4627],
  [4627],
  [4627],
  [4627],
  [4627],
  [4627],
  [4627],
  [4627],
  [4627],
  [4627],
  [4627],
  [4627],
  [5444],
  [5444],
  [5444],
  [5444],
  [5444],
  [5444],
  [5444],
  [5444],
  [5444],
  [5444],
  [5444],
  [5444],
  [5444],
  [5444],
  [5444],
  [5444],
  [5444],
  [5444],
  [5444],
  [5444],
  [5444],
  [5444],
  [5444],
  [5444],
  [5444],
  [5444],
  [5444],
  [5444],
  [5444],
  [5444],
  [5444],
  [5444],
  [5444],
  [5444],
  [5444],
  [5444],
  [5444],
  [5444],
  [5444],
  [5444],
  [5444],
  [5444],
  [7314],
  [7314],
  [7314],
  [7314],
  [7314],
  [7314],
  [7314],
  [7314],
  [7314],
  [7314],
  [7314],
  [7314],
  [7314],
  [7314],
  [7314],
  [7314],
  [7314],
  [7314],
  [7314],
  [7314],
  [7314],
  [7314],
  [7314],
  [5551],
  [5551],
  [5551],
  [5551],
  [5551],
  [5551],
  [5551],
  [5551],
  [5551],
  [5551],
  [5551],
  [5551],
  [5551],
  [5551],
  [5551],
  [5551],
  [5551],
  [5551],
  [5551],
  [5551],
  [5551],
  [5551],
  [5551],
  [5551],
  [5551],
  [5551],
  [5551],
  [5551],
  [5551],
  [5551],
  [5551],
  [5551],
  [5551],
  [5551],
  [5551],
  [5551],
  [5551],
  [5551],
  [5551],
  [5551],
  [5551],
  [5551],
  [5551],
  [5551],
  [5551],
  [5551],
  [5551],
  [5551],
  [5551],
  [5551],
  [5551],
  [5551],
  [5551],
  [5551],
  [5551],
  [5551],
  [5551],
  [5551],
  [5551],
  [5551],
  [5551],
  [5551],
  [5551],
  [5551],
  [5551],
  [5551],
  [5551],
  [5551],
  [5551],
  [5551],
  [5551],
  [5551],
  [5551],
  [5551],
  [5551],
  [5551],
  [5551],
  [5551],
  [5551],
  [5551],
  [5551],
  [5551],
  [5551],
  [5551],
  [5551],
  [5551],
  [5551],
  [5551],
  [5778],
  [5778],
  [5778],
  [5778],
  [5778],
  [5778],
  [5778],
  [5778],
  [5778],
  [5778],
  [5778],
  [5778],
  [5778],
  [5778],
  [5778],
  [5778],
  [5778],
  [5778],
  [5778],
  [5778],
  [5778],
  [5778],
  [5778],
  [5778],
  [5778],
  [5778],
  [5778],
  [5778],
  [5778],
  [5778],
  [5778],
  [5778],
  [5778],
  [5778],
  [5778],
  [5778],
  [5778],
  [5778],
  [5778],
  [5778],
  [5778],
  [5778],
  [5778],
  [5778],
  [5778],
  [5778],
  [5778],
  [5778],
  [5778],
  [5778],
  [5778],
  [5778],
  [5778],
  [5778],
  [5778],
  [5778],
  [5778],
  [5778],
  [5778],
  [5778],
  [5778],
  [5778],
  [5778],
  [5778],
  [6141],
  [6141],
  [6141],
  [6141],
  [6141],
  [6141],
  [6141],
  [6141],
  [6141],
  [6141],
  [6141],
  [6141],
  [6141],
  [6141],
  [6141],
  [6141],
  [6141],
  [6141],
  [6141],
  [6141],
  [6141],
  [6141],
  [6141],
  [6141],
  [6141],
  [6141],
  [6141],
  [6141],
  [6141],
  [6141],
  [6141],
  [6141],
  [6141],
  [6141],
  [6141],
  [6141],
  [6141],
  [6141],
  [6141],
  [6141],
  [6141],
  [6100],
  [6100],
  [6100],
  [6100],
  [6100],
  [6100],
  [6100],
  [6100],
  [6100],
  [6100],
  [6100],
  [6100],
  [6100],
  [6100],
  [6100],
  [6100],
  [6100],
  [6100],
  [6100],
  [6100],
  [6100],
  [5775],
  [5775],
  [5775],
  [5775],
  [5775],
  [5775],
  [5775],
  [5775],
  [5775],
  [5775],
  [5775],
  [5775],
  [5775],
  [5775],
  [5775],
  [5775],
  [5775],
  [5775],
  [5775],
  [5775],
  [5829],
  [5829],
  [5829],
  [5829],
  [5829],
  [5829],
  [5829],
  [5829],
  [5829],
  [5829],
  [5829],
  [5829],
  [5829],
  [5829],
  [5829],
  [5829],
  [5829],
  [5829],
  [5829],
  [5829],
  [5829],
  [5829],
  [5829],
  [5829],
  [5829],
  [5840],
  [6535],
  [6628],
  [6432],
  [6537],
  [6537]
])

# create NeuralNetwork class
class NeuralNetwork:

    # intialize variables in class
    def __init__(self, inputs, outputs):
        self.inputs = inputs
        self.outputs = outputs
        # initialize weights as .50 for simplicity.
        # IMPORTANT: When adding additional paramaters to the input, also add additional rows to the following array
        self.weights = np.array([[.50]])
        self.error_history = []
        self.epoch_list = []

    #activation function ==> S(x) = 1/1+e^(-x)
    def sigmoid(self, x, deriv=False):
        if deriv == True:
            return x * (1 - x)
        return 1 / (1 + np.exp(-x))

    # data will flow through the neural network.
    def feed_forward(self):
        self.hidden = self.sigmoid(np.dot(self.inputs, self.weights))

    # going backwards through the network to update weights
    def backpropagation(self):
        self.error  = self.outputs - self.hidden
        delta = self.error * self.sigmoid(self.hidden, deriv=True)
        self.weights += np.dot(self.inputs.T, delta)

    # train the neural net for 25,000 iterations
    def train(self, epochs=25000):
        for epoch in range(epochs):
            # flow forward and produce an output
            self.feed_forward()
            # go back though the network to make corrections based on the output
            self.backpropagation()
            # keep track of the error history over each epoch
            self.error_history.append(np.average(np.abs(self.error)))
            self.epoch_list.append(epoch)

    # function to predict output on new and unseen input data
    def predict(self, new_input):
        prediction = self.sigmoid(np.dot(new_input, self.weights))
        return prediction

# create neural network
NN = NeuralNetwork(inputs, outputs)
# train neural network
NN.train()

# create two new examples to predict
example = np.array([int(input("Input current price in USD: "))])

# print the predictions for both examples
print('Support Price Prediction: ', NN.predict(example))
# print(inputs.shape)
# print(outputs.shape)

# plot the error over the entire training duration
# plt.figure(figsize=(15,5))
# plt.plot(NN.epoch_list, NN.error_history)
# plt.xlabel('Epoch')
# plt.ylabel('Error')
# plt.show()