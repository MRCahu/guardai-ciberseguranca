"""Banco efêmero com uma conta fictícia; sem rede ou arquivos persistentes."""
import sqlite3


def make_database():
    connection = sqlite3.connect(":memory:")
    connection.execute("CREATE TABLE users (username TEXT PRIMARY KEY, password TEXT NOT NULL)")
    connection.execute("INSERT INTO users VALUES (?, ?)", ("aluno", "senha-sintetica"))
    return connection
