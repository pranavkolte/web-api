import config
import hashlib


def getSHA(password):
    SHA_password = hashlib.sha256(password.encode('utf-8')).hexdigest().upper()
    return SHA_password


def signup(username, password, IP):
    try:
        database = config.get_database()
        cursor = database.cursor()
        cursor.execute(config.QUERRY_SIGNUP,
                       (username, getSHA(password), "ON", IP))
        database.commit()
        return True
    except:
        database.rollback()
        return False
    finally:
        database.close()


if __name__ == '__main__':
    print(signup("user2", "123456", "192.168.50.25"))
