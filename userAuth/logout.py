import config


def logout(userID):
    try:
        database = config.get_database()
        cursor = database.cursor()
        cursor.execute(config.QUERRY_LOGOUT, ('OFF', userID))
        database.commit()
        return True
    except:
        database.rollback()
        return False
    finally:
        database.close()


if __name__ == '__main__':
    print(logout(1))
