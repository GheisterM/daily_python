from menu import Menu
from money_machine import MoneyMachine
from coffee_maker import CoffeeMaker
import os


def clear():
    """Clears the console."""

    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


if __name__ == '__main__':

    clear()

    m_menu = Menu()
    m_money = MoneyMachine()
    m_maker = CoffeeMaker()
    MENU_ITEMS = m_menu.get_items().rstrip("/")
    COMMANDS = m_menu.get_items().split('/')
    COMMANDS.extend(['off', 'report'])
    turned_on = True
    while turned_on:
        PROMPT = f'What would you like? ({MENU_ITEMS}):'
        order = input(PROMPT).lower()

        if order == 'off':
            turned_on = False
        elif order == 'report':
            m_maker.report()
            m_money.report()
        else:
            item = m_menu.find_drink(order)
            if item is not None:
                if m_maker.is_resource_sufficient(item):
                    if m_money.make_payment(item.cost):
                        m_maker.make_coffee(item)
