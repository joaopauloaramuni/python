# ASCII Clock

Este projeto implementa um relógio digital que exibe a hora atual utilizando caracteres ASCII em um estilo semelhante ao mostrado no filme "Matrix". A hora é atualizada a cada segundo e exibida em verde vibrante no terminal.

## Como funciona

O relógio digital é renderizado utilizando um conjunto de caracteres ASCII representando os números de 0 a 9. A cada segundo, a hora é obtida no formato HHMMSS e exibida no terminal com a cor verde, utilizando códigos ANSI para colorir o texto.

### Exemplo de saída

A hora será exibida da seguinte forma no terminal:

```
 _    _    _    _    _    _   
| |  |_|   _|  |_|   _|   _|  
|_|  |_|  |_   |_|  |_   |_   
```

## Como rodar o projeto

### Pré-requisitos

- Python 3.x instalado.
- O terminal precisa suportar códigos ANSI para colorir o texto.

### Passos para executar

1. Clone ou baixe o repositório.
2. Abra o terminal na pasta do projeto.
3. Execute o arquivo Python:

```bash
python main.py
```

A hora será exibida em um estilo de relógio digital no terminal, atualizando-se a cada segundo.

## Como funciona o código

1. **Mapeamento ASCII**: Cada número de 0 a 9 é representado por uma lista de três strings que formam o número no estilo digital.
2. **Coloração**: O texto é colorido em verde usando códigos ANSI para simular o estilo de "Matrix".
3. **Atualização a cada segundo**: A hora é obtida usando `time.strftime('%H%M%S')`, e o terminal é limpo a cada segundo para exibir a hora atualizada.

## Licença

Este projeto está licenciado sob a MIT License.
