# -*- coding: utf-8 -*-
"""Building_LSTM_Model.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ETRAr4yGVC3S6O9H1ZBiLNrxoX9FllB1

Build and Train the LSTM Model
"""

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout

# Build the LSTM model
model = Sequential()

# Add LSTM layers
model.add(LSTM(units=50, return_sequences=True, input_shape=(X.shape[1], X.shape[2])))
model.add(Dropout(0.2))
model.add(LSTM(units=50, return_sequences=False))
model.add(Dropout(0.2))

# Output layer
model.add(Dense(units=1))  # Predict the next closing price

# Compile the model
model.compile(optimizer='adam', loss='mean_squared_error')

# Train the model
model.fit(X, y, epochs=20, batch_size=32)