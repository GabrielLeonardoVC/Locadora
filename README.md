Locação
O sistema de Locação de Jogos e Filmes é um código em Python usando POO que permite com que gerencie os clientes, jogos e filmes deixando-os práticos. É possível fazer o cadastro de clientes, registra os itens para a locação, controla os empréstimos e devolução e também acompanha a disponibilidade dos itens,

======= TERMINAR ================




O projeto foi desenvolvido utilizando conceitos de Programação Orientada a Objetos (POO), como herança e encapsulamento, especificamente como exemplo para estudos de POO e oferecendo uma experiência completa de como uma locadora funciona de forma estruturada e eficiente.

2️⃣ Estrutura do Projeto 👨‍💻

O sistema é organizado em arquivos específicos para manter o código modular, claro e fácil de manter:

2.1 - itens.py 🎬🎮

Defina como classes Item, Filme e Jogo, com todos os atributos e métodos necessários para locação, devolução e controle de disponibilidade.

2.2 - cliente.py 👤

Contém a classe Cliente, permitindo alugar, devolver e listar os itens que cada cliente possui.

2.3 - locadora.py 🏢

Classe Locadora, responsável por gerenciar listas de clientes e itens, oferecendo métodos para cadastrar, listar e controlar locações.

2.4 - main.py 🚀

Arquivo principal com o menu interativo, integrando todas as funcionalidades do sistema e permitindo que o usuário:

Cadastro de clientes;

Cadastre filmes ou jogos;

Listar clientes e itens disponíveis;

Realizar locações e devoluções;

Insira o sistema.

2.5 - README.md 📃

Documentação completa do projeto, explicando cada classe, método e funcionalidade inovadora.

3️⃣ Programação do Projeto 💻

O sistema foi desenvolvido utilizando POO em Python, garantindo modularidade e claramente no código.

3.1 Arquivos e Funções Principais 📂

main.py

Menu interativo para integrar todas as funcionalidades.

Loop contínuo até que a escolha do usuário saia, com tratamento de abordagens.

funcoes.py Funções auxiliares que conectam o menu às operações das classes:

cadastrar_cliente(locadora) → adicionar um cliente;

cadastrar_item(locadora) → adicionar um Filme ou Jogo com todos os atributos;

locar_item(locadora) → permite alugar um item disponível;

devolver_item(locadora) → permite devolver um item localizado.

3.2 Classes e Estrutura de Dados 🏢🎬🎮

Item (base de classe)

Atributos: codigo, titulo, disponivel

Métodos: alugar() e devolver()

Filme (herda de Item)

Atributos adicionais: genero, duração

Jogo (herda de Item)

Atributos adicionais: plataforma, faixa_etaria

Cliente

Atributos: nome, cpf, itens_locados

Métodos:

localizar(item) → adicionar item à lista se estiver disponível

devolver(item) → remover item da lista e atualizar disponibilidade

listar_itens() → exibe itens localizados

Locadora

Atributos: clientes, itens

Métodos:

cadastrar_cliente(cliente)

cadastrar_item(item)

listar_clientes()

listar_itens() (status exibe: Disponível / Alugado)

3.3 Funcionamento do Sistema ⚙️

Cadastro: Clientes e itens são registrados no sistema;

Listagem: Visualização de clientes e itens disponíveis;

Localização: O cliente seleciona o item disponível, que é adicionado à sua lista e marcado como oferecido;

Devolução: Cliente devolve item, que é removido da lista e marcado como disponível;

Menu interativo: Todas as ações são realizadas através do menu, tornando o uso intuitivo e controlado.

4️⃣ Conclusão ✅

O Sistema de Locadora de Filmes e Jogos demonstra a aplicação prática de POO em Python, utilizando conceitos como herança, encapsulamento e modularidade.

Com ele, é possível:

Gerenciar clientes, filmes e jogos;

Controlar empréstimos e devoluções;

Filtrar itens por diferentes critérios;

Ter uma visão completa de como uma locadora funciona.

O projeto serve como um excelente recurso educacional, permitindo compreender a interação entre objetos e a importância de organizar código de forma clara.

Ele pode ser expandido facilmente, adicionando persistência em banco de dados, interface gráfica ou novas funcionalidades, tornando-o uma base sólida para aprendizado e desenvolvimento de sistemas mais complexos.
