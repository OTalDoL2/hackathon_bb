from connection import supabase

def lista_usuario():
    usuarios = supabase.table("usuarios").select('*').execute()


def create_user(usuario):
    # print(usuario.to_json())
    supabase.table("usuarios").insert({"nome": usuario.nome, "cpf": usuario.documento, "data_nascimento": usuario.data_nascimento, "email": usuario.email, "pontuacao": usuario.pontuacao}).execute()

def create_pedidos(user_id, produtos):
    