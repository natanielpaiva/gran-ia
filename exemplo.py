import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

# 1. Criar o modelo sequencial
modelo = keras.Sequential([
    layers.Dense(16, activation='relu', input_shape=(10,)),  # 10 é o número de entradas
    layers.Dense(8, activation='relu'),
    layers.Dense(1, activation='sigmoid')  # Saída binária: 0 ou 1
])