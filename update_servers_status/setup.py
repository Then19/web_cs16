def create_config():
    answer = input('Create new config? y/n ')
    if not answer in 'Yy':
        return
    user = input('db user: ')
    password = input('db password: ')
    db_name = input('db name: ')
    with open('config.py', 'w', encoding='utf-8') as file:
        file.write(f'SQL_LOGIN = "mysql+mysqlconnector://{user}:{password}@localhost/{db_name}?charset=utf8"')


if __name__ == "__main__":
    create_config()
