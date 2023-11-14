from database import Database

class TeacherCRUD:
    def __init__(self, uri, user, password):
        self.db = Database(uri, user, password)

    def create(self, name, ano_nasc, cpf):
        self.db.execute_query("CREATE (:Teacher {name: $name, ano_nasc: $ano_nasc, cpf: $cpf})", {"name": name, "ano_nasc": ano_nasc, "cpf": cpf})

    def read(self, name):
        resultado = self.db.execute_query("MATCH (t:Teacher {name: $name}) RETURN t", {"name": name})
        return resultado
    
    def update(self, name, new_cpf):
        self.db.execute_query("MATCH (t:Teacher {name: $name}) SET t.cpf = $new_cpf", {"name": name, "new_cpf": new_cpf})

    def delete(self, name):
        self.db.execute_query("MATCH (t:Teacher {name: $name}) DETACH DELETE t", {"name": name})

    def close(self):
        self.db.close