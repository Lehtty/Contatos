import contatos_utilis

try:
    #contatos = contatos_utilis.csv_para_contatos('C:/Users/letic/PycharmProjects/contatos/dados/contatos.csv')
    #contatos_utilis.contatos_para_pickle(contatos,'C:/Users/letic/PycharmProjects/contatos/dados/contatos.pickle' )

    #contatos = contatos_utilis.pickle_para_contatos('C:/Users/letic/PycharmProjects/contatos/dados/contatos.pickle')
    #contatos_utilis.contatos_para_json(contatos, 'C:/Users/letic/PycharmProjects/contatos/dados/contatos.json')

    contatos = contatos_utilis.json_para_contatos('C:/Users/letic/PycharmProjects/contatos/dados/contatos.json')

    for contato in contatos:
        print(f'{contato.id} - {contato.nome} - {contato.email}')

except FileNotFoundError:
    print('Arquivo não encontrado')
except PermissionError:
    print('sem permissão de escrita')
