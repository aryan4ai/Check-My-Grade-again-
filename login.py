import base64
import csv

class LoginUser:
    def __init__(self, email_id, password, role):
        self.email_id = email_id
        self.password = password
        self.role = role

    def encrypt_password(self, plain):
        return base64.b64encode(plain.encode()).decode()

    def decrypt_password(self, encrypted):
        return base64.b64decode(encrypted.encode()).decode()

    def login(self, email, password):
        with open("data/login.csv", "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row["user_id"] == email:
                    if self.decrypt_password(row["password"]) == password:
                        print("Login successful.")
                        return True
        print("Invalid credentials.")
        return False

    def logout(self):
        print("Logged out.")

    def change_password(self, email, old_password, new_password):
        rows = []
        with open("data/login.csv", "r") as f:
            reader = csv.DictReader(f)
            fieldnames = reader.fieldnames
            for row in reader:
                if row["user_id"] == email:
                    if self.decrypt_password(row["password"]) == old_password:
                        row["password"] = self.encrypt_password(new_password)
                rows.append(row)
        with open("data/login.csv", "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)
        print("Password updated.")