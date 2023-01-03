import config


def isLoggedIn(userID, userIP):
    try:
        database = config.get_database()
        cursor = database.cursor()
        cursor.execute(config.QUERRY_CHECK_LOGIN_STATUS, (userID,))
        result = cursor.fetchall()
        if result:
            IP = result[0][0]
            status = result[0][1]
            if IP == userIP and status == 'ON':
                return True
            else:
                return False
    except:
        return False
    finally:
        database.close()


def isUsernameValid(username):
    try:
        database = config.get_database()
        cursor = database.cursor()
        cursor.execute(config.QUERRY_ISUSERNAME_VALID, (username,))
        response = cursor.fetchall()
        if response:
            return True
        else:
            return False
    except:
        return False
    finally:
        database.close()


if __name__ == '__main__':
    # print(isLoggedIn(1, '192.168.50.25'))
    print(isUsernameValid('akh'))
