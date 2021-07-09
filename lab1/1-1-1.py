import numpy as np
from tensorflow.keras import models
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras import optimizers

study_time = np.array([1,2,3,4,5,6])
results = np.array([10,20,30,40,50,60])

model = Sequential()
model.add( Dense(1, input_dim=1, activation = 'linear') )

sgd = optimizers.SGD(lr = 0.01)
model.compile(optimizer = sgd, loss='mse', metrics=['accuracy'])

model.fit(study_time, results, batch_size=1, epochs=100, shuffle = False)

print(model.predict([7]))
