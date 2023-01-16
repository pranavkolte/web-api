import mysql.connector
import hashlib
import socket

# ----------------local------------------
DATABASE_SERVER_HOST = '127.0.0.1'
DATABASSE_USER = 'root'
DATABASE_NAME = 'api-local'
DATABASSE_PASSWORD = ''


QUERRY_CHECK_LOGIN_STATUS = "SELECT IP, status FROM login WHERE ID=%s"
QUERRY_SIGNUP = "INSERT INTO login (username, password, status, IP) VALUES(%s,%s,%s,%s)"
QUERRY_ISUSERNAME_VALID = "SELECT username FROM login WHERE username=%s"
QUERRY_LOGIN = "SELECT ID, username, password FROM login WHERE username=%s AND password= %s"
QUERRY_SET_LOGIN_STATUS = "UPDATE login SET IP=%s, status=%s WHERE ID=%s"
QUERRY_CHECK_USERNAME = "SELECT username FROM login WHERE username=%s"
QUERRY_CHECK_PASSWORD = "SELECT password FROM login WHERE username=%s"
QUERRY_RESET_PASSWORD = "UPDATE login SET password=%s WHERE username=%s"
QUERRY_LOGOUT = "UPDATE login SET status=%s WHERE ID=%s"

CURRENT_IP = socket.gethostbyname(socket.gethostname())


def get_database():
    mydatabase = mysql.connector.connect(
        host=DATABASE_SERVER_HOST,
        user=DATABASSE_USER,
        password=DATABASSE_PASSWORD,
        database=DATABASE_NAME,
    )
    if mydatabase:
        return mydatabase
    else:
        print('Cannot connect to database :-(')
        return None


def getSHA(password):
    SHA_password = hashlib.sha256(password.encode('utf-8')).hexdigest().upper()
    return SHA_password


if __name__ == '__main__':
    print(get_database())
