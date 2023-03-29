class Arquivo:
    def __init__(self):
        pass

    def escrever(self, arquivo='', content=''):
        if arquivo or content:
            nome = arquivo
            texto = content
        else:
            nome = input("DIGITE O NOME DO ARQUIVO\n" +
                         "(não é necessário informar extensão '.txt')\nNome do Arquivo: \n")
            texto = input("Digite o texto: ")

        with open(f'Atividade sobre manipulação de arquivos/{nome}.txt', 'a') as f:
            f.write(f'{texto}\n')

    def vogais(self, palavra):
        vogais = 0
        lista_vogais = ['a', 'e', 'i', 'o', 'u']
        for char in palavra:
            if char.lower() in lista_vogais:
                vogais += 1
        return vogais

    def consoantes(self, palavra):
        consoantes = 0
        lista_consoantes = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm',
                            'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
        for char in palavra:
            if char.lower() in lista_consoantes:
                consoantes += 1
        return consoantes

    def ler(self):
        qnt = int(input("Quantos arquivos você irá passar?\nQuantidade: "))
        with open('Atividade sobre manipulação de arquivos/SAIDAS.txt', 'a') as saida:
            for i in range(qnt):
                nome = input("\nDIGITE O NOME DO ARQUIVO\n" +
                             "(não é necessário informar extensão '.txt')\nNome do Arquivo: ")
                try:
                    with open(f'Atividade sobre manipulação de arquivos/{nome}.txt', 'r') as f:
                        linhas = f.readlines()
                        linhasQNT = len(linhas)
                        palavrasQNT = 0
                        caracteresQNT = 0
                        vogais = 0
                        consoantes = 0
                        for linha in linhas:
                            palavras = linha.split()
                            palavrasQNT += len(palavras)
                            for palavra in palavras:
                                vogais += self.vogais(palavra)
                                consoantes += self.consoantes(palavra)
                                caracteresQNT += len(palavra)
                        caracteres_especiais = caracteresQNT - vogais - consoantes
                    saida.write(f'O arquivo {nome}:\n')
                    saida.write(f'A quantidade de linhas é {linhasQNT}\n')
                    saida.write(f'A quantidade de palavras é {palavrasQNT}\n')
                    saida.write(f'A quantidade de caracteres é {caracteresQNT}\n')
                    saida.write(f'A quantidade de vogais é {vogais}\n')
                    saida.write(f'A quantidade de consoantes é {consoantes}\n')
                    saida.write(f'A quantidade de caracteres especiais é {caracteres_especiais}\n\n')
                except FileNotFoundError:
                    print("Arquivo não encontrado.")


    def substituir_string(arquivo_origem, arquivo_destino, string_padrao, string_substituta):
        with open(arquivo_origem, 'r') as f_origem:
            conteudo = f_origem.read()
            conteudo_substituido = conteudo.replace(string_padrao, string_substituta)

        with open(arquivo_destino, 'w') as f_destino:
            f_destino.write(conteudo_substituido)
