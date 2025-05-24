from datetime import datetime, timedelta
import json

path = "D:\\Ghost\\Usuário\\Desktop\\cursopy2025\\projeto_paralelo\\database.json" #path significa caminho, que é o diretório do banco de dados
#primeiro, vamos precisar ver se tem algo no json
def main():
    with open(path, 'r') as read_arch: #ler arquivo a tradução
        try:
            data = json.load(read_arch) #se a base de dados estiver vazia, o código quebra
            #para garantir que isso não ocorra, fazemos uso do try e do except
        except (json.JSONDecodeError):
            data = [] #nesse caso, criamos uma lista.

    #agora vamos escrever no documento.
    with open(path, 'w') as write_arch: #escrever no arquivo
        #questionando o usuário
        name = input('Qual é o seu nome? ')
        age = input('Qual é a sua idade? ')
        gender = input('Qual é o seu gênero? ')
        time = datetime.now().timestamp() #armazenando a data e a hora que o usuário escreveu
        dici = {key:value for key, value in (('Name', name), ('Age', age), ('Gender', gender), ('Time', time))}
        #o dicionário comprehension acima é para alinhar as variáveis    
        data.append(dici) #adiciono na lista
        #e agora é só adicionar no json
        json.dump(data, write_arch, indent=2)

if __name__ == '__main__':
    main()
    














    
    
    
    
    
    
#     [
#   {
#     "Name": "v",
#     "Age": "4",
#     "Gender": "4",
#     "Time": 1748095421.727798
#   }
# ]
    
    
    
    
    
    
    
    

# mensagem = 'Olá, tudo bem?'

# fmt = '%d/%m/%Y %H:%M:%S'
# hora = datetime.now()
# marca_temporal = datetime.timestamp(hora)
# print(marca_temporal)
