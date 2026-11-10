import unittest
from lab.database import make_database
from lab.app import login as vulnerable
from lab.app_secure import login as secure


class AuthenticationTests(unittest.TestCase):
    def setUp(self):
        self.db = make_database()

    def tearDown(self):
        self.db.close()

    def test_valid_login_both_versions(self):
        for login in (vulnerable, secure):
            self.assertTrue(login(self.db, "aluno", "senha-sintetica"))

    def test_invalid_password_both_versions(self):
        for login in (vulnerable, secure):
            self.assertFalse(login(self.db, "aluno", "incorreta"))

    def test_comment_bypass_reproduced_and_blocked(self):
        self.assertTrue(vulnerable(self.db, "aluno' -- ", "incorreta"))
        self.assertFalse(secure(self.db, "aluno' -- ", "incorreta"))

    def test_tautology_blocked(self):
        self.assertTrue(vulnerable(self.db, "' OR 1=1 -- ", "x"))
        self.assertFalse(secure(self.db, "' OR 1=1 -- ", "x"))

    def test_empty_fields_blocked(self):
        self.assertFalse(secure(self.db, "", ""))

    def test_quote_in_legitimate_username(self):
        self.db.execute("INSERT INTO users VALUES (?, ?)", ("d'agua", "teste"))
        self.assertTrue(secure(self.db, "d'agua", "teste"))

    def test_unknown_user_blocked(self):
        self.assertFalse(secure(self.db, "inexistente", "senha-sintetica"))

    def test_destructive_text_is_only_data(self):
        self.assertFalse(secure(self.db, "'; DROP TABLE users; --", "x"))
        self.assertEqual(self.db.execute("SELECT COUNT(*) FROM users").fetchone()[0], 1)


if __name__ == "__main__":
    unittest.main()
