"""Correção do vetor SQL Injection. Não é autenticação pronta para produção."""


def login(connection, username, password):
    query = "SELECT username FROM users WHERE username = ? AND password = ?"
    return connection.execute(query, (username, password)).fetchone() is not None
