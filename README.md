# Algoritmo de Eleição de líder em anel
O algoritmo de eleição de líder em anel é um algoritmo distribuído que permite a eleição de um líder em um anel de processos. O algoritmo é baseado em mensagens trocadas entre os processos e é utilizado para garantir a exclusão mútua em sistemas distribuídos.

- **Objetivo**:
   - Implementar o algoritmo de eleição de líder em anel.

- **Características**:
   - Cada nó possui um identificador único.
   - Os nós são organizados em um anel.
   - O algoritmo é baseado em mensagens trocadas entre os processos.


- **Tecnologias Utilizadas**:
   - Python 3.13

- **Como executar o projeto**:

   - Clone o repositório:
       ```
       git clone https://github.com/matheus1103/algoritmo-de-eleicao.git
      ```
   - Acesse o diretório do projeto:
       ```
       cd algoritmo-de-eleicao
      ```
   - Execute o arquivo main.py:
       ```
       python main.py
      ```
- **Exemplo de uso**:
   - Após executar o arquivo main.py, será exibida a tela inicial do programa. Nessa tela, o usuário deve clicar no botão "Start Election" para iniciar a eleição de líder em anel ou "Fail Random Process" para encerrar um processo e iniciar automaticamente uma nova eleição.
![alt text](/images/tela.png)
- **Autor**:
   - Matheus Francisco Rodrigues Lima - 19104064