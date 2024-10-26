from functools import wraps

def input_error(handler):
    @wraps(handler)
    def inner(*args, **kwargs):
        try:
            return handler(*args, **kwargs)
        except KeyError:
            return 'Contact not found. Please enter a valid contact name.'
        except ValueError:
            return 'Please enter the correct number of arguments.'
        except IndexError:
            return 'Incomplete information provided. Please provide all necessary details.'
    return inner


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
def add_contact(args, contacts):
    name, phone = args
    if name not in contacts:
        contacts[name] = phone
        return 'Contact added.'
    else:
        return f'Contact with name "{name}" already exists.'


@input_error
def change_contact(args, contacts):
    name, phone = args

    if contacts[name]:
        contacts[name] = phone
        return 'Contact changed.'


@input_error
def get_contact_phone(args, contacts):
    name = args[0]
    return f'{name}: {contacts[name]}'


@input_error
def get_all_contacts(contacts):
    if contacts:
        return '\n'.join(f"{name}: {phone}" for name, phone in contacts.items())
    else:
        return 'The contact list is empty.'


def main():
    contacts = {}
    print('Welcome to the assistant bot!')
    while True:
        user_input = input('Enter a command: ')

        if not user_input:
            print("Please enter a valid command.")
            continue

        command, *args = parse_input(user_input)
        match command:
            case 'close' | 'exit':
                print('Good bye!')
                break
            case 'hello':
                print('How can I help you?')
            case 'add':
                print(add_contact(args, contacts))
            case 'change':
                print(change_contact(args, contacts))
            case 'phone':
                print(get_contact_phone(args, contacts))
            case 'all':
                print(get_all_contacts(contacts))
            case _:
                print('Invalid command.')


if __name__ == '__main__':
    main()
