import config


def checkUserID(username):
    database = config.get_database()
    mycursor = database.cursor()
    mycursor.execute(
        config.QUERRY_CHECK_USERNAME, (username,))
    response = mycursor.fetchall()
    if response:
        return True
    else:
        return False


def checkPassword(username, oldpass):
    database = config.get_database()
    mycursor = database.cursor()
    mycursor.execute(
        config.QUERRY_CHECK_PASSWORD, (username,))
    response = mycursor.fetchall()

    if not response:
        return False

    if response[0][0] == config.getSHA(oldpass):
        return True
    return False


def resetPassword(username, new_password,):
    database = config.get_database()
    mycursor = database.cursor()
    mycursor.execute(config.QUERRY_RESET_PASSWORD,
                     (config.getSHA(new_password), username))
    database.commit()
    return True


if __name__ == '__main__':
    print(checkPassword("user", "123456"))
    # print(checkUserID('user'))
    # print(resetPassword("user", '654321'))
