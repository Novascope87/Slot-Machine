import random
from typing import Dict, List, Tuple

MAX_SLOTS = 5
LIMIT_BET = 1000
LIMIT_MIN = 10

ROWS = 5
COLS = 5

symbol_count: Dict[str, int] = {
    'A': 2,
    'B': 4,
    'C': 9,
    'D': 2
}
symbol_values: Dict[str, int] = {
    'A': 5,
    'B': 4,
    'C': 3,
    'D': 2
}

def winnings(columns: List[List[str]], slots: int, bet: int, values: Dict[str, int]) -> tuple[int, list[int]]:
    winning = 0
    winning_lines = []
    for line in range(slots):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:  # This else belongs to the for, executed if no break occurs
            winning += values[symbol] * bet
            winning_lines.append(line + 1)
    return winning, winning_lines

def slot_machine_spin(rows: int, cols: int, symbols: Dict[str, int]) -> List[List[str]]:
    all_symbols = []
    for symbol, count in symbols.items():
        all_symbols += [symbol] * count
    columns = []
    for _ in range(cols):
        col = random.sample(all_symbols, rows)
        columns.append(col)
    return columns

def print_slot_machine(columns: List[List[str]]):
    for row in range(ROWS):
        print(' | '.join(column[row] for column in columns))

def get_deposit() -> int:
    while True:
        amount = input("How much would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                return amount
            else:
                print("The amount must be greater than 0.")
        else:
            print("Please enter a valid amount.")

def how_many_slots() -> int:
    while True:
        slots = input(f"Enter the number of lines to bet on (1-{MAX_SLOTS}): ")
        if slots.isdigit():
            slots = int(slots)
            if 1 <= slots <= MAX_SLOTS:
                return slots
            else:
                print(f"Please enter a number between 1 and {MAX_SLOTS}.")
        else:
            print("Please enter a valid number.")

def get_place() -> int:
    while True:
        amount = input(f"How much would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if LIMIT_MIN <= amount <= LIMIT_BET:
                return amount
            else:
                print(f"Amount must be between ${LIMIT_MIN} and ${LIMIT_BET}.")
        else:
            print("Please enter a valid number.")

def main():
    balance = get_deposit()
    slots = how_many_slots()
    keep_playing = True

    while keep_playing:
        place = get_place()
        total_bet = place * slots
        if total_bet > balance:
            print(f"You do not have enough to bet that amount, your balance is: ${balance}")
            break  # Exit the game if the bet cannot be placed
        else:
            balance -= total_bet
            print(f"You are betting ${place} on each of the {slots} lines. Total bet is: ${total_bet}")

            machine = slot_machine_spin(ROWS, COLS, symbol_count)
            print_slot_machine(machine)
            winning, winning_lines = winnings(machine, slots, place, symbol_values)
            balance += winning
            print(f'You won ${winning}')
            print(f'Winning lines:', *winning_lines)
            print(f'Your new balance is: ${balance}')

            # Ask if the player wants to continue
            continue_playing = input("Do you want to keep spinning? (yes/no): ").lower()
            if continue_playing != "yes":
                keep_playing = False

if __name__ == "__main__":
    main()