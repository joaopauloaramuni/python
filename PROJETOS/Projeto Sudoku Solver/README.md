# Algoritmo resolvedor de Sudoku com backtracking | Sudoku Solver

**Última atualização no Geeks for Geeks:** 31 de janeiro de 2025

Dado um Sudoku incompleto na forma de matriz `mat[][]` de ordem 9×9, a tarefa é completar o Sudoku.

Uma solução de Sudoku deve satisfazer todas as seguintes regras:

- Cada um dos dígitos de 1 a 9 deve ocorrer exatamente uma vez em cada linha.
- Cada um dos dígitos de 1 a 9 deve ocorrer exatamente uma vez em cada coluna.
- Cada um dos dígitos de 1 a 9 deve ocorrer exatamente uma vez em cada uma das 9 subgrades 3×3 da matriz.

**Nota:** Zeros na `mat[][]` indicam espaços em branco, que devem ser preenchidos com algum número entre 1 e 9. Você não pode substituir o elemento em uma célula que não esteja em branco.

---

## Exemplos:

| <img src="https://joaopauloaramuni.github.io/python-imgs/Sudoku_Solver_With_Backtracking/imgs/Suduko-example-question.png" alt="Input" width="600"/> | <img src="https://joaopauloaramuni.github.io/python-imgs/Sudoku_Solver_With_Backtracking/imgs/Suduko-example-answer.png" alt="Output" width="600"/> |
|:------:|:-----:|
| Input | Output | 

**Explicação:** Cada linha, coluna e caixa 3×3 da matriz de saída contém números únicos.

---

## [Abordagem Ingênua] Usando Backtracking

A ideia é usar backtracking e gerar recursivamente todas as configurações possíveis de números de 1 a 9 para preencher as células vazias da matriz `mat[][]`.

Para isso, para cada célula não atribuída, preencha a célula com um número de 1 a 9, um por um. Após preencher a célula não atribuída, verifique se a matriz é segura ou não. Se for segura, vá para a próxima célula; caso contrário, retroceda (backtrack) para testar outros casos.

Para verificar se é seguro colocar o valor `num` na célula `mat[i][j]`, percorra todas as colunas da linha `i`, todas as linhas da coluna `j` e a subgrade 3×3 que contém a célula `(i, j)` e verifique se já possuem o valor `num`. Se sim, retorne `false`, caso contrário, retorne `true`.

**Complexidade de Tempo:** `O(n * 9^(n*n))`  
Para cada índice não atribuído, há 9 opções possíveis e, para cada índice, estamos verificando outras colunas, linhas e caixas.

**Espaço Auxiliar:** `O(1)`

---

## [Abordagem Esperada] Usando Bitmasking com Backtracking — `O(9 * n * n)` Tempo e `O(n)` Espaço

Na abordagem acima, a função `isSafe()` (usada para verificar se é seguro colocar o número `num` na célula `(i, j)`) pesquisa o `num` em cada linha, coluna e caixa.

A ideia é otimizar isso usando **Bitmasking**. Para isso, crie três arrays: `rows[]`, `cols[]` e `boxs[]`, de tamanho `n`, para marcar os valores já utilizados na linha, coluna e caixa, respectivamente.

O elemento `rows[i]` marca os números já utilizados na linha `i`, e o mesmo vale para `cols[]` e `boxs[]` para colunas e caixas. Para marcar o número `num` na linha `i`, defina o bit correspondente ao `num` da esquerda para a direita em `rows[i]` e proceda de forma semelhante para `cols[]` e `boxs[]`.

Da mesma forma, para desmarcar o valor `num`, desfaça os bits definidos no passo atual.

**Complexidade de Tempo:** `O(9 * n * n)`  
**Espaço Auxiliar:** `O(n)`

---