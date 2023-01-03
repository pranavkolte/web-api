import mysql.connector
import socket


# DATABASE_SERVER_HOST = 'remotemysql.com'
# DATABASSE_USER = 'LKxXNksPlP'
# DATABASE_NAME = 'LKxXNksPlP'
# DATABASSE_PASSWORD = 'LGh76olfte'

# ----------------local------------------
DATABASE_SERVER_HOST = '127.0.0.1'
DATABASSE_USER = 'root'
DATABASE_NAME = 'api-local'
DATABASSE_PASSWORD = ''

PORT = '3360'
QUERRY_CHECK_LOGIN_STATUS = "SELECT IP, status FROM login WHERE ID=%s"
QUERRY_ISUSERNAME_VALID = "SELECT username FROM login WHERE username=%s"
QUERRY_LOGIN = "SELECT ID, username, password FROM login WHERE username=%s AND password= %s"
QUERRY_SET_LOGIN_STATUS = "UPDATE login SET IP=%s, status=%s WHERE ID=%s"
QUERRY_LOGOUT = "UPDATE login SET status=%s WHERE ID=%s"
QUERRY_GET_PATIENT = "SELECT ID, name, mobile, gender, age, medical_history, address from patient"
QUERRY_ADD_PATIENT = "INSERT INTO patient (name, gender, age, mobile, address, medical_history) VALUES (%s, %s, %s, %s, %s, %s)"
QUERRY_UPDATE_PATIENT = "UPDATE patient SET name=%s, gender=%s, age=%s, mobile=%s, address=%s, medical_history=%s WHERE ID=%s"
QUERRY_UPDATE_PATIENT_NAME = "UPDATE patient SET name=%s WHERE ID=%s"
QUERRY_UPDATE_PATIENT_GENDER = "UPDATE patient SET gender=%s WHERE ID=%s"
QUERRY_UPDATE_PATIENT_AGE = "UPDATE patient SET age=%s WHERE ID=%s"
QUERRY_UPDATE_PATIENT_MOBILE = "UPDATE patient SET mobile=%s WHERE ID=%s"
QUERRY_UPDATE_PATIENT_ADDRESS = "UPDATE patient SET address=%s WHERE ID=%s"
QUERRY_UPDATE_PATIENT_MEDICAL_HISTORY = "UPDATE patient SET medical_history=%s WHERE ID=%s"

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


if __name__ == '__main__':
    print(get_database())
