# Ler o conteúdo da Lista A e Lista B
with open('Seguir editando.txt', 'r', encoding='utf-8') as arquivo_a, open('teste.txt', 'r', encoding='utf-8') as arquivo_b:
    lista_completa = arquivo_a.read()
    lista_vazia = arquivo_b.read()

# Dividir os parágrafos em ambas as listas
lista_completa = lista_completa.split('\n\n')
lista_vazia = lista_vazia.split('\n\n')

# Criar um dicionário para mapear nomes e números de CNH aos parágrafos em Lista A
registros_novos = {}
for p in lista_completa:
    info = p.split('CPF')
    try:
        news = info[1]
        olds = info[0]
        index = 0
        if len(olds.split(',')[1].split(' ')[5]) == 11:
            index = 5
        else:
            index = 4
        chave = f"{olds.split(',')[0]},{olds.split(',')[1].split(' ')[index]}"
        registros_novos[chave] = news
    except:
        continue

# Atualizar Lista B com informações de Lista A
for n, p in enumerate(lista_vazia):
    info = p.split(',')
    nome = info[0]
    lista = info[1].split(' ')
    for i in lista:
        if len(i) == 11:
            cnh = i
    chave = f'{nome},{cnh}'
    info_cpf_a = registros_novos.get(chave, "Sem info.")
    lista_vazia[n] = f'{nome},{cnh}\n{info_cpf_a}'

# Unir os parágrafos e salvar a nova Lista B
texto = '\n\n'.join(lista_vazia)

with open('teste cheio.txt', 'w', encoding='utf-8') as arquivo_saida:
    arquivo_saida.write(texto)
