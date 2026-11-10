"""EXEMPLO INTENCIONALMENTE VULNERÁVEL. Usar somente no laboratório em memória."""


def login(connection, username, password):
    query = f"SELECT username FROM users WHERE username = '{username}' AND password = '{password}'"
    return connection.execute(query).fetchone() is not None
