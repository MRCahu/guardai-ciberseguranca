"""Execute a partir da raiz: python3 -m lab.demo."""
from lab.database import make_database
from lab.app import login as vulnerable
from lab.app_secure import login as secure


def main():
    connection = make_database()
    try:
        cases = [("válido", "aluno", "senha-sintetica"),
                 ("senha incorreta", "aluno", "incorreta"),
                 ("bypass sintético", "aluno' -- ", "incorreta")]
        for label, username, password in cases:
            print(f"{label}: vulnerável={vulnerable(connection, username, password)}; parametrizado={secure(connection, username, password)}")
    finally:
        connection.close()


if __name__ == "__main__":
    main()
