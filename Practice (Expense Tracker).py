# Adding a new dictionary to the list
def add_an_expense(expenses_list,amount,category):
    # Same category check
    sc_check = 0
    # Looking for same category inside expenses list
    for dictionary in expenses_list:
        if category == dictionary['category']:
            dictionary['amount'] = float(dictionary['amount']) + float(amount)
            sc_check = 1
    if sc_check == 0:
        expenses_list.append({'amount': amount, 'category': category})

def all_expenses(expenses_list):
    for expense in expenses_list:
        # Calling out a dictionary (named 'expense' in a loop) element value with key 'amount'
        print(f'Amount: {expense['amount']}, Category: {expense['category']}')


def total_expenses(expenses_list):
    return sum(map(lambda expense: float(expense['amount']),expenses_list))


def category_filter(expenses_list, chosen_category):
    return filter(lambda expense: expense['category'] == chosen_category, expenses_list)

# Main function that calls menu and takes input
def main():
    # A list of dictionaries as elements of it
    expenses_list = []
    while True:
        print('\nExpense Tracker')
        print('1. Add an expense')
        print('2. List all expenses')
        print('3. Show total expenses')
        print('4. Filter expenses by category')
        print('5. Exit')
        choice = input('Enter your choice: ')
        if choice == '1':
            amount = input('Enter amount: ')
            category = input('Enter category: ')
            print (add_an_expense(expenses_list,amount,category))
        if choice == '2':
            print('\n All Expenses:')
            all_expenses(expenses_list)
        if choice == '3':
            print(total_expenses(expenses_list))
        if choice == '4':
            chosen_category = input('Enter category you want to see: ')
            print(f'\nExpenses for {chosen_category}: ')
            expenses_for_category = category_filter(expenses_list,chosen_category)
            all_expenses(expenses_for_category)
        if choice == '5':
            print ('Exiting the program...')
            break
main()