# This is a sample Python script.
import socket


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

connections_db = {}  # {'username': ConnectionObj}


def byte_string_decode(string):
    return string.decode('utf-8')


def is_username(msg):
    return msg[0] == '[' and msg[-1] == ']'


def receive_message(conn):
    return byte_string_decode(conn.recv(1024))


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('', 55000))
    sock.listen(10)
    print('Server is running, please press ctrl+c to stop')
    while True:
        conn, addr = sock.accept()
        print('connected:', addr)

        msg = receive_message(conn)
        if is_username(msg):
            connections_db[msg] = conn
            conn.send(bytes(f'Hello, {msg}\n', encoding='UTF-8'))
        else:
            for _, c in connections_db:
                c.send(bytes(msg, encoding='UTF-8'))









#def username_given(conn):
    # data = conn.recv(1024)
    # username = str(data)[2:-3]
    # if username in users_db:
    #     conn.send(bytes(f'Name {username} is already occupied, please provide another name\n', encoding='UTF-8' ))
    #     return username_given(conn)
    # else:
    #     users_db[username] = { 'messages_count': 0 }
    #     conn.send(bytes(f'Hello, {username}\n', encoding='UTF-8'))
    #     return username


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
