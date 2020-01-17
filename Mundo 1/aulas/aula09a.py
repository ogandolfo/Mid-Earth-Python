# fatiamento
frase = 'Curso em Vídeo Python'
frase2 = '   Aprenda Python  '

print(frase[9:21])  # exibe informações em um intervalo
print(frase[9:21:2])  # exibe informações em um intervalo saltando 'casa'
print(frase[:5])  # exibe informações em um intervalo partindo do início
print(frase[15:])  # exibe informações em um intervalo até o final
print(frase[9::3])   # exibe informações em um intervalo até o final saltando 'casas'

# análise
print(len(frase))  # comprimento da frase em caracteres
print(frase.count('o'))  # contar quantos CARACTERES ESPECÍFICOS existem na frase
print(frase.count('o', 0, 13))  # exibe quantos CARACTERES ESPECÍFICOS existem na frase aplicando fatiamento
print(frase.find('deo'))  # exibe o momento em que o TERMO tem início
print(frase.find('Android'))  # exibe o valor negativo caso a STRING não exista
print('Curso' in frase)  # exibe T ou F para a existência da STRING na frase

# transformação
print(frase.replace('Python', 'Android'))  # substitui um termo
print(frase.upper())  # permite colocar a frase em LETRAS MAIÚSCULAS
print(frase.lower())  # permite colocar a frase em LETRAS MINÚSCULAS
print(frase.capitalize())  # permite colocar apenas a primeira letra em UPPER enquanto as outras ficam LOWER
print(frase.title())  # permite colocar inicial de palavra em UPPER e mantém as demais em LOWER
print(frase2.strip())  # permite remover espaços ANTES e DEPOIS de uma frase
print(frase2.rstrip())  # permite remover os espaços à DIREITA da string
print(frase2.lstrip())  # permite remover os espações à ESQUERDA da string

# divisão de string
dividido = (frase.split())  # permite zerar a contagem de 'casas' por meio dos espaços entre termos e divide as # PALAVRAS em grupos
print(dividido)

# junção
print('-'.join(dividido))

# printar um texto que usa mais que uma linha
print("""Pode utilizar a Galeria de peças rápidas para criar, armazenar e reutilizar partes de conteúdo, incluindo
texto automático, propriedades do documento (como título e autor) e campos. Estes blocos de conteúdo
reutilizáveis também são chamados de blocosmodulares. O texto automático é um tipo de bloco de
construção comum que armazena texto e gráficos. Pode utilizar o organizador de blocos modulares
para localizar ou editar um bloco modular.""")
