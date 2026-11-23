Controle de Estoque em Python

Programa feito em Python, que roda no terminal, para controlar uma lista de produtos de estoque. Cada produto é guardado como texto no formato produto = marca, e tudo é feito por um menu que se repete até o usuário escolher sair.

Os produtos que aparecem no programa são apenas exemplos.

Menu

O programa mostra um menu em um laço while True e repete até a opção de sair:
Opção	O que faz
1) Cadastrar	Adiciona um produto novo
2) Mostrar	Mostra todos os produtos
3) Remover	Remove um produto escolhido pelo número
4) Modificar	Remove ou troca o nome de um produto escolhido pelo número
5) Buscar	Procura um produto e oferece cadastrá-lo se não existir
6) Sair	Encerra o programa

Qualquer outra opção mostra o aviso "Opção inválida".

O que cada função faz

Cadastrar: pede o produto e a marca, deixa o texto em minúsculas e tira espaços das pontas. Se o produto já existe na lista, avisa e não duplica. Se não existe, adiciona.

Mostrar: percorre a lista e imprime um produto por linha. Se a lista estiver vazia, avisa que ainda não há produtos.

Remover: mostra a lista numerada a partir de 1 e pede o número do produto. O programa confere se o que foi digitado é um número e se ele está entre 1 e o total de produtos. Se estiver, remove pela posição e mostra qual produto saiu. Se a lista estiver vazia, avisa e encerra a função.

Modificar: mostra a lista numerada e pede o número do produto. Depois pergunta o que fazer:

Remover o produto
Trocar pelo nome novo que o usuário digitar

Opção inválida, número fora da lista ou texto no lugar do número mostram um aviso.

Buscar: mostra a lista e pede o produto procurado. Se encontrar, mostra o item. Se não encontrar, avisa e pergunta se o usuário quer cadastrá-lo (s ou n).

Validações
Entradas de texto passam por .lower().strip(), então "Pão de Forma " e "pão de forma" são tratados como o mesmo produto.

Ao escolher um produto pelo número, o programa só aceita números válidos e avisa nos outros casos.

A lista vazia é tratada em Mostrar, Remover e Modificar.

Conceitos de Python usados
Listas (append, pop, len, troca por posição)
Funções com def e return
while True e break
if, elif e else, inclusive um if dentro do outro
for e enumerate
Conversão de texto em número com int() e conferência com .isdigit()
Comparação encadeada, como 1 <= numero <= len(Estoque)

Autor

Vinícius Sales Freitas
