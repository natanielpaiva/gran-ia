# Código para treinar o modelo com os dados de treinamento

modelo.fit(
    X_train,          # Dados de entrada para o treinamento
    y_train,          # Rótulos correspondentes aos dados de entrada
    epochs=10,        # Número de épocas para o treinamento
    batch_size=32     # Tamanho do lote para cada iteração
)