import psycopg2

class Connection():

    def get_connection(self):
        connection = psycopg2.connect(user="postgres",
                                      password="1234",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="N3")
        print("Database Connected")
        return connection