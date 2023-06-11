Autores: Henrique Xavier, Leonardo Oliveira e Lucas Antunes
Versão: Python 3.8.10

# Tutorial
Execute o código com o seguinte comando:

```
python main.py <cifra> <operação> <parâmetros>
```

## Cifras:
- AES (aes)
- 3DES (3des)

## Operações
- Efeito avalanche (avalanche)
- Entropia da imagem
- Criptografar matriz RGB da image
- Descriptografia matriz RGB da imagem
- Histograma da imagem

### Efeito Avalanche
Calcula o criterio de avalanche para uma cifra.

#### Parâmetros
- Rodadas de criptografia

#### Exemplos:
```
python main.py aes avalanche 10
```

### Entropia da Imagem
Calcula a entropia de uma imagem.

#### Parâmetros
- Caminho (path) para a imagem

#### Exemplos:
```
python main.py aes entropy images/fruits.png
```

### Criptografar Matriz RGB da Imagem
Criptografa a matriz RGB de uma imagem.

#### Parâmetros
- Caminho (path) para a imagem

#### Exemplos:
```
python main.py aes enc-image images/fruits.png
```

*Nota: É gerada uma chave durante a execução que pode ser usada na descriptografia da imagem.*

### Descriptografia Matriz RGB da Imagem
Descriptografa a matriz RGB de uma imagem.

#### Parâmetros
- Caminho (path) para a imagem
- Chave

#### Exemplos:
```
python main.py aes dec-image images/encrypted_fruit.png 8D1C74A1B85F5908E8FECC104FBA
```

### Histograma da Imagem
Gera o histograma de uma imagem.

#### Parâmetros
- Caminho (path) para a imagem

#### Exemplos:
```
python main.py aes histogram images/fruits.png
```

### Tempo para Criptografar Matriz RGB da Imagem
Calcula o tempo médio de 15 criptografias da matriz RGB de uma imagem.

#### Parâmetros
- Caminho (path) para a imagem

#### Exemplos:
```
python main.py aes time images/fruits.png
```