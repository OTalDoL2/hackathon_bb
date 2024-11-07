class Usuario:
    def __init__(self):
        self.nome = ''
        self.documento = ''
        self.endereço = ''
        self.senha = ''
        self.pontuacao = ''
        self.email = ''
        self.data_nascimento = ''
        
    def novo_usuario(self, nome, documentacao, email, data_nascimento):
        self.nome = nome
        self.documento = documentacao
        self.pontuacao = 0
        self.email = email
        self.data_nascimento = data_nascimento




