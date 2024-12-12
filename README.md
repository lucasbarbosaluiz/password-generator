# Gerador de Senha TryCatch

## Descrição

O **Gerador de Senha TryCatch** é uma aplicação gráfica simples desenvolvida com Python usando a biblioteca `Tkinter`. Ela permite gerar senhas seguras com base nas preferências do usuário, incluindo a escolha de caracteres maiúsculos, minúsculos, números e caracteres especiais. O aplicativo oferece um controle de comprimento da senha e exibe uma barra de progresso para indicar a força da senha gerada.

## Funcionalidades

- Geração de senhas com diferentes combinações de:
  - Caracteres maiúsculos (A-Z)
  - Caracteres minúsculos (a-z)
  - Números (0-9)
  - Caracteres especiais (como !, @, #, etc.)
  
- A senha gerada pode ser copiada para a área de transferência com um clique.
- A interface gráfica é intuitiva e permite fácil interação através de checkboxes e um controle deslizante para ajustar o comprimento da senha.
- A barra de progresso indica a "força" da senha com base nas opções escolhidas pelo usuário.

## Tecnologias

- Python 3.x
- Tkinter (Biblioteca para GUI)
- pyperclip (Biblioteca para copiar para a área de transferência)
- random (Biblioteca para gerar senhas aleatórias)
- string (Biblioteca para manipulação de strings)

## Requisitos

- Python 3.x instalado na máquina.
- Bibliotecas necessárias:
  - Tkinter (geralmente já vem instalado com Python)
  - pyperclip

Para instalar a biblioteca `pyperclip`, use o seguinte comando:

```bash
pip install pyperclip
