# Importa as funções criadas anteriormente
from biblioteca_refatorada import *
from banco_de_dados import *
# Define a função para exibir o menu e receber a entrada do usuário
def show_menu():
    print("Selecione uma opção:")
    print("1. Inserir um novo livro")
    print("2. Inserir um novo usuário")
    print("3. Exibir todos os usuarios")
    print("4. Realizar um empréstimo")
    print("5. Atualizar a data de devolução de um empréstimo")
    print("6. Exibir todos os livros emprestados no momento")
    print("7. Exibir todos os livros do banco de dados")
    print("0. Sair")

    choice = input("Digite o número da opção desejada: ")
    return choice

# Loop principal do programa
while True:
    choice = show_menu()

    if choice == "1":
        title = input("Digite o título do livro: ")
        author = input("Digite o nome do autor do livro: ")
        publisher = input("Digite o nome da editora do livro: ")
        year = input("Digite o ano de publicação do livro: ")
        isbn = input("Digite o ISBN do livro: ")

        insert_book(title, author, publisher, year, isbn)
        print("Livro inserido com sucesso!")

    elif choice == "2":
        first_name = input("Digite o primeiro nome do usuário: ")
        last_name = input("Digite o sobrenome do usuário: ")
        address = input("Digite o endereço do usuário: ")
        email = input("Digite o endereço de e-mail do usuário: ")
        phone = input("Digite o número de telefone do usuário: ")

        insert_user(first_name, last_name, address, email, phone)
        print("Usuário inserido com sucesso!")

    elif choice == '3':
        print("Listando todos os usuários...\n")
        users = get_users()
        for user in users:
            print(f"ID: {user[0]}\nNome: {user[1]}\nTelefone: {user[5]}\nEmail: {user[4]}\n")


    elif choice == "4":
        user_id = input("Digite o ID do usuário: ")
        book_id = input("Digite o ID do livro: ")

        insert_loan(user_id, book_id, None, None)
        print("Empréstimo realizado com sucesso!")

    elif choice == "5":
        loan_id = input("Digite o ID do empréstimo: ")
        return_date = input("Digite a nova data de devolução (formato: AAAA-MM-DD): ")

        update_loan_return_date(loan_id, return_date)
        print("Data de devolução atualizada com sucesso!")

    elif choice == "6":
        books_on_loan = get_books_on_loan()
        print("Livros emprestados no momento:")
        for book in books_on_loan:
            print(f"ID empréstimo: {book[0]},Título: {book[1]}, Nome do usuário: {book[2]} {book[3]}, Data do empréstimo: {book[4]}, Data da devolução: {book[5]}")

    elif choice == "7":
        books = get_books()
        print("Livros:")
        for book in books:
            print(f"Título: {book[1]}, Autor: {book[2]}, Editora: {book[3]}, Ano: {book[4]}, ISBN: {book[5]}")

    elif choice == "0":
        break

    else:
        print("Opção inválida. Por favor, selecione uma opção válida.")