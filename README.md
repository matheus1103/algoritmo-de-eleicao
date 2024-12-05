# Algoritmo de Eleição de líder em anel
O algoritmo de eleição de líder em anel é um algoritmo distribuído que permite a eleição de um líder em um anel de processos. O algoritmo é baseado em mensagens trocadas entre os processos e é utilizado para garantir a exclusão mútua em sistemas distribuídos.

- **Objetivo**:
   - Implementar o algoritmo de eleição de líder em anel.

- **Características**:
   - Cada nó possui um identificador único.
   - Os nós são organizados em um anel.
   - O algoritmo é baseado em mensagens trocadas entre os processos.
   - O processo a ser encerrado será aleatório, também será aleatório o processo que irá identificar a falha e iniciar a eleição.

- **Funcionamento (Pseudocódigo)**:
   ```
      INICIALIZAR:
   Cada processo tem um ID único.
   Os processos estão organizados em um anel lógico.
   Um processo detecta a falha do líder atual e inicia a eleição.

   ALGORITMO DE ELEIÇÃO:
   Processo iniciador envia uma mensagem de ELEIÇÃO para o próximo processo no anel:
      Mensagem contém uma lista de IDs de processos participantes.

   Enquanto a mensagem não retorna ao iniciador:
      O processo que recebe a mensagem:
         - Adiciona seu ID à lista de IDs na mensagem.
         - Envia a mensagem para o próximo processo no anel.

   Quando a mensagem retorna ao iniciador:
      - O iniciador seleciona o maior ID da lista como o novo líder.
      - Envia uma mensagem de LÍDER ao próximo processo no anel.

   ALGORITMO DE PROPAGAÇÃO DO LÍDER:
   Cada processo que recebe a mensagem de LÍDER:
      - Atualiza seu registro para indicar o novo líder.
      - Repassa a mensagem ao próximo processo no anel.

   Quando a mensagem de LÍDER retorna ao iniciador:
      - A eleição está concluída e todos os processos sabem quem é o novo líder.

   FIM DO ALGORITMO

   ```
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
- **Exemplo de uso**: Após executar o arquivo main.py, será exibida a tela inicial do programa. Nessa tela, o usuário deve clicar no botão "Start Election" para iniciar a eleição de líder em anel ou "Fail Random Process" para encerrar um processo e iniciar automaticamente uma nova eleição.


## Tela inicial do programa
![Inicio do codigo](/images/tela.png)
## Tela após falhar um processo e iniciar a eleição
![Inicio do codigo](/images/tela2.png)
## Tela após eleição de líder
![Inicio do codigo](/images/tela3.png)

- **Autor**:
   - Matheus Francisco Rodrigues Lima - 19104064