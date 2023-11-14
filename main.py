from database import Database
from query import QueryQuestoes
from teacherCRUD import TeacherCRUD
from CLI import CLI


db = Database('neo4j+s://50718b33.databases.neo4j.io','neo4j','vXKcrpKbrBxPdKmLAa9XRONWDGbpxq4w798kLVra3d4')
queries = QueryQuestoes(db)
#Aqui tem a execução de todas as queries das questoes 1 e 2. Deixei comentado pra não bagunçar tudo
#depois que eu fui testar, tá dando um erro bizarro na execução mesmo com as querys certas (testei no neo4j e funcionou mas aqui não, fala que as chaves não existem)
#result = queries.query1a()
#print(result)
#result = queries.query1b()
#print(result)
#result = queries.query1c()
#print(result)
#result = queries.query1d()
#print(result)
#result = queries.query2a()
#print(result)
#result = queries.query2b()
#print(result)
#result = queries.query2c()
#print(result)
#result = queries.query2d()

#questão 3 letra a ta no arquivo chamado teacherCRUD.py
#crudteach = TeacherCRUD('neo4j+s://50718b33.databases.neo4j.io','neo4j','vXKcrpKbrBxPdKmLAa9XRONWDGbpxq4w798kLVra3d4')

#3 letra b
#crudteach.create("Chris Lima", 1956, "189.052.396-66")

#3 letra c12
#busca = crudteach.read("Chris Lima")
#print(busca)

#3 letra d
#crudteach.update("Chris Lima","162.052.777-77")

#3 letra e
menuzitcho = CLI()
menuzitcho.menu()