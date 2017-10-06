import vk


APP_ID = 6210230


def get_user_login():
    return input('Enter your login: ')


def get_user_password():
    return input('Enter your password: ')


def get_online_friends(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
        scope='friends'
    )
    api = vk.API(session)
    friends = api.friends.getOnline()
    return api.users.get(user_ids=friends)


def output_friends_to_console(friends_online):
    for friend in friends_online:
        print('{} {}'.format(friend['first_name'], friend['last_name']))


if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    friends_online = get_online_friends(login, password)
    output_friends_to_console(friends_online)
