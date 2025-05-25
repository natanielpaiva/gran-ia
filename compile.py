modelo.compile(
    optimizer='adam',               # Otimizador que ajusta os pesos
    loss='binary_crossentropy',     # Função de perda para classificação binária
    metrics=['accuracy']            # Métrica de desempenho
)