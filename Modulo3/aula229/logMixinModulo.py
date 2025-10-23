####################
# Atenção -> Abaixo, há uma cópia da aula 228.
# Para ser mais específico, da parte de logMixin.

class Log:
    def log(self, msg): 
        # Esse método serve apenas como modelo para as subclasses.
        raise NotImplementedError('Você não deve usar essa classe diretamente. Use a classe filha.')
    
    # método de error que vai retornar o método log com o Erro
    def log_error(self, msg):
        return self.log(f'Error: {msg}')
    
    # método de suceso que vai retornar o método log com o sucesso
    def log_sucess(self, msg):
        return self.log(f'Sucess: {msg}')
    
# Classe concreta que implementa a abstração
class LogMixin(Log):
    def log(self, msg):
        print(msg)

#########
# Agora, vamos utilizar a classe que criamos para realizar o salvamento 
# de arquivos. Para isso, vamos precisar de uma nova classe, que será filha.

from pathlib import Path # importanto path para manipulação caminhos
from datetime import datetime # esse eu vou usar para adicionar o momento do log.
from zoneinfo import ZoneInfo # esse será para passar o timezone

# crio a classe e herdo a classe Log
class LogFileMixin(Log):
    # sobrescrevendo o método log
    def log(self, msg):
        # busca o caminho que o código foi executado e volta para trás uma vez
        caminho_atual = Path(__file__).parent
        # denomina um caminho para o arquivo de log
        arquivo_log = caminho_atual / 'aula228LogFileMixin.txt' 

        # passando o tz de SP
        tz_SP = ZoneInfo('America/Sao_Paulo')
        
        # buscando a hora atual com o tz e formatando
        agora = datetime.now(tz=tz_SP).strftime('%d/%m/%Y %H:%M:%S')

        # utiliza context maneger para escrita de em arquivos
        with open(arquivo_log, 'a') as f:
            f.write(f'{agora} -> {msg}')
            f.write('\n')