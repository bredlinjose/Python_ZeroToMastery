# parameters
def say_hello(name, emoji):
    print(f'Hello {name} {emoji}')


# positional arguments
say_hello('Bredlin', '😁')  # Hello Bredlin 😁
say_hello('Akash', '😁')  # Hello Akash 😁

# keyword argument
say_hello(emoji='😒', name='Jose')  # Hello Jose 😒


# Default parameters
def say_hai(name='Bredlin Jose', emoji='🤦‍♂️'):
    print(f'Hai {name} {emoji}')


say_hai('Caffrey', '😜')  # Hai Caffrey 😜
say_hai()  # Hai Bredlin Jose 🤦‍♂️
say_hai('Dev')  # Hai Dev 🤦‍♂️
say_hai(emoji='😎')  # Hai Bredlin Jose 😎
