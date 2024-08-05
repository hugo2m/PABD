import psycopg2

# Conexão ao banco de dados
conn = psycopg2.connect(
    dbname="AtividadesBD",
    user="user",
    password="password",
    host="localhost",
    port="5432"
)

cursor = conn.cursor()

# Inserir uma atividade
cursor.execute(
    "INSERT INTO atividades (projeto_id, descricao) VALUES (%s, %s)", (1, 'Nova Atividade'))

# Atualizar o líder de um projeto
cursor.execute("UPDATE projetos SET lider = %s WHERE id = %s",
               ('Novo Líder', 1))

# Listar todos os projetos e suas atividades
cursor.execute(
    "SELECT p.id, p.nome, p.lider, a.descricao FROM projetos p LEFT JOIN atividades a ON p.id = a.projeto_id")
resultados = cursor.fetchall()

for linha in resultados:
    print(linha)

conn.commit()
cursor.close()
conn.close()
