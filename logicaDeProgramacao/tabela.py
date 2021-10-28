#Crie um arquivo com algumas linhas de texto no seu editor de arquivos texto preferido
#(por exemplo: Bloco de Notas, Gedit, Emacs) e depois crie um programa para ler essas
#linhas e mostrá-las no console.

atualizacao = "Estou aprendendo lógica e python\n" \
              "e estou aprendendo muito, e ando\n" \
              "muito interessada em desenvolvimento\n" \
              "também é muito trabalhoso, mas não\n a " \
              "desafio que não possa ser quebrado XD"\

def escrever_texto(texto):
    arquivo = open('C:\\temp\\texto.txt', 'w')
    arquivo.write(texto)
    arquivo.close()


def ler_texto(nome_arquvio):
    arquivo = open('C:\\temp\\texto.txt', 'r')
    texto = arquivo.read()
    print(texto)

def atualizar_texto(texto):
    arquivo = open('C:\\temp\\texto.txt', 'a')
    arquivo.write(atualizacao)
    arquivo.close()

if __name__ == '__main__':
    escrever_texto('{}\n'.format(atualizacao))
    ler_texto('texto.txt')