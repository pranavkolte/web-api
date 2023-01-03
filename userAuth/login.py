import hashlib
import config


def getSHA(password):
    SHA_password = hashlib.sha256(password.encode('utf-8')).hexdigest().upper()
    return SHA_password


def login(username, password):
    try:

        database = config.get_database()
        if not database:
            print('something wrong with connection')
            return False

        mycursor = database.cursor()
        mycursor.execute(config.QUERRY_LOGIN, (username, getSHA(password)))
        result = mycursor.fetchall()
        status = "ON"
        userID = result[0][0]

        if result:
            mycursor.execute(config.QUERRY_SET_LOGIN_STATUS,
                             (config.CURRENT_IP, status, userID))
            database.commit()
            return True
        else:
            return False

    except:
        database.rollback()
        return False
    finally:
        database.close()


if __name__ == '__main__':
    print(login('user', '123456'))
    # print(check_status())
