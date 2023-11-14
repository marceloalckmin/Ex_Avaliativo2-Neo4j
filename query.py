from database import Database

class QueryQuestoes:
    def __init__(self,database):
        self.db = database
    
    def query1a(self):
        query = "match(n:Teacher) where n.name = 'Renzo' return n.ano_nasc, n.cpf;"
        results = self.db.execute_query(query)
        [(result.get("ano_nasc", None), result.get("cpf", None)) for result in results]
    
    def query1b(self):
        query = "match (n:Teacher) where n.name starts with 'M' return n.name, n.cpf"
        results = self.db.execute_query(query)
        return [(result["name"], result["cpf"]) for result in results]
    
    def query1c(self):
        query = "match (n:City) return distinct n.name"
        results = self.db.execute_query(query)
        return [result["name"] for result in results]
    def query1d(self):
        query = "match(n:School) where n.number>=150 and n.number<=550 return n.name,n.address,n.number"
        results = self.db.execute_query(query)
        return [(result["name"], result["address"], result["number"]) for result in results]
    def query2a(self):
        query1 = "match (n:Teacher) return min(n.ano_nasc)"
        results1 = self.db.execute_query(query1)
        query2 = "match (n:Teacher) return max(n.ano_nasc)"
        results2 = self.db.execute_query(query2)
        resultado = [results1, results2]
        return resultado
    def query2b(self):
        query = "match (n:City) return AVG(n.population)"
        results = self.db.execute_query(query)
        return results
    def query2c(self):
        query = "match(n:City) where n.cep = '37540-000' return replace(n.name, 'a', 'A')"
        results = self.db.execute_query(query)
        return results
    def query2d(self):
        query = "match (n:Teacher) return substring(n.name, 3, 1)"
        results = self.db.execute_query(query)
        return results
    