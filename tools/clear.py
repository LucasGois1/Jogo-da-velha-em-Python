import os


def clear():
    """Limpar o console"""
    return os.system('cls' if os == 'nt' else 'clear')
