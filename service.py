from connection import Connection

class crud():
    
    def save(self, dados_dict):

        nome = dados_dict.get("nome")
        cpf = dados_dict.get("cpf")
        email = dados_dict.get("email")

        self.validate_nome(nome)
        self.validate_cpf(cpf)
        self.validate_email(email)
        self.validate_must_have(nome, cpf, email)

        conn = Connection().get_connection()

        cur = conn.cursor()
        cur.execute ("insert into person (nome, cpf, email, logado) values ('{0}','{1}','{2}', '1')".format(nome, cpf, email))

        conn.commit()
        conn.close()

    def ver_todos(self):
        conn = Connection().get_connection()

        cur = conn.cursor()
        cur.execute("select * from person where logado = '1'")

        rows = cur.fetchall()

        nova_lista=[]

        for row in rows:
            dicionario1 = {"id":row[0], "nome":row[1], "cpf":row[2], "email":row[3]}
            nova_lista.append(dicionario1)

        conn.close()
        return nova_lista


    def listar_cpf(self, dados_dict):
   
        cpf = dados_dict.get("cpf")

        self.validate_cpf(cpf)

        conn = Connection().get_connection()

        cur = conn.cursor()
        cur.execute("select * from person where logado = '1' AND cpf = '{0}'".format(cpf))

        rows = cur.fetchall()

        nova_lista = []
        for row in rows:
            dicionario1 = {"id": row[0], "nome": row[1], "cpf": row[2], "email": row[3]}
            nova_lista.append(dicionario1)
            
        conn.commit()
        conn.close()

        return nova_lista


    def listar_email(self, dados_dict):

        email = dados_dict.get("email")

        self.validate_email(email)

        conn = Connection().get_connection()

        cur = conn.cursor()
        cur.execute("select * from person where logado = '1' AND email = '{0}'".format(email))

        rows = cur.fetchall()

        nova_lista = []
        for row in rows:
            dict_01 = {"id": row[0], "nome": row[1], "cpf": row[2], "email": row[3]}
            nova_lista.append(dict_01)

        conn.commit()
        conn.close()

        return nova_lista


    def update_nome(self, dados_dict):
        
        cpf = dados_dict.get("cpf")
        self.validate_cpf(cpf)

        nome = dados_dict.get("nome")
        self.validate_nome(nome)

        conn = Connection().get_connection()

        cur = conn.cursor()
        cur.execute("Update person set nome = '{0}' WHERE cpf = '{1}' AND logado = '1'".format(nome, cpf))

        conn.commit()
        conn.close()

    def update_email(self, dados_dict):

        cpf = dados_dict.get("cpf")
        self.validate_cpf(cpf)

        email = dados_dict.get("email")
        self.validate_email(email)

        conn = Connection().get_connection()

        cur = conn.cursor()
        cur.execute("Update person set email = '{0}' WHERE cpf = '{1}' AND logado = '1'".format(email, cpf))
        conn.commit()
        conn.close()

    def deletar_cpf(self, dados_dict):

        cpf = dados_dict.get("cpf")
        self.validate_cpf(cpf)

        conn = Connection().get_connection()

        cur = conn.cursor()
        cur.execute("Update person set logado = '0' WHERE cpf = '{0}' AND logado = '1'".format(cpf))
        conn.commit()

        conn.close()

    def validate_email(self, email):
        if len(email) <= 400:
            print("Email válido.")
            return 1
        else:
            print("Email inválido.")
            return 0

    def validate_nome(self, nome):
        if len(nome) <= 150:
            print("Nome válido.")
            return 1
        else:
            print("Nome inválido.")
            return 0

    def validate_cpf(self, cpf):
        if cpf.isdigit() == True and len(cpf) == 11:
            print("CPF válido.")
            return 1
        else:
            print("CPF inválido.")
            return 0

    def validate_must_have(self, nome, cpf, email):
        if nome is None:
            raise Exception("A inserção do nome é necessária.")
        if cpf is None:
            raise Exception("A inserção do CPF é necessária.")
        if email is None:
            raise Exception("A inserção do email é necessária.")