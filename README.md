# Sistema de Locadora de Filmes e Jogos

Este projeto é um sistema simples de locação de filmes e jogos, desenvolvido em **Python**, utilizando **Programação Orientada a Objetos (POO)**.  

O sistema permite:

- Cadastrar clientes, filmes e jogos  
- Listar clientes e itens disponíveis  
- Realizar empréstimos e devoluções de itens  
- Controlar a disponibilidade dos itens alugados  

---

## Estrutura do Projeto

O projeto está organizado em três arquivos principais:

### 1. `classes.py`

Define todas as classes do sistema:

- **Item**: Classe base para filmes e jogos  
- **filme(Item)**: Representa filmes, possui gênero  
- **jogo(Item)**: Representa jogos, possui faixa etária  
- **cliente**: Representa clientes, controla itens alugados  
- **locadora**: Controla o cadastro de clientes e itens, além de fornecer métodos para listagem e busca  

Exemplo de uso das classes:

`python
cliente1 = cliente("João", "12345678900")
filme1 = filme(1, "Matrix", "Ficção")
cliente1.locar(filme1)

## 2. `funcoes.py`

Contém funções que implementam a lógica do sistema:

- `cadastrarocliente()`: Cadastro de novos clientes  
- `cadastroitem()`: Cadastro de filmes ou jogos  
- `listaroclientes()`: Exibe clientes cadastrados  
- `listaritens()`: Exibe itens cadastrados e sua disponibilidade  
- `emprestaritem()`: Realiza o empréstimo de um item para um cliente  
- `devolveritem()`: Permite devolver um item alugado  

> O arquivo utiliza a instância global `locadoraa` da classe `locadora`.

---

## 3. `app.py`

Arquivo principal que executa o menu interativo:

- Menu com opções numeradas de 1 a 7  
- Utiliza **match-case** para tratar as escolhas do usuário  
- Validação de entrada para evitar erros ao digitar caracteres não numéricos  
- Limpeza da tela (`cls`) e pausa (`pause`) para melhor experiência  
