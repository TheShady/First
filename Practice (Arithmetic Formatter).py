def arithmetic_arranger(problem_list,solution_check=False):
# Rule 1
    if len(problem_list) > 5:
        print("Error: Too many problems.")
        return
# Rule 2
    for _ in problem_list:
        if '/' in _ or '*' in _:
            print('Error: Operator must be '+' or '-'.')
            return
# Getting all the elements + Rule 3
    sign_list = []
    operand1_list = []
    operand2_list = []
    max_len_list = []
    for problem in problem_list:
        if "+" in problem:
            sign_list.append('+')
        elif '-' in problem:
            sign_list.append('-')
        operands = problem.split(' ')
        for operand in operands:
# Rule 4
            if len(operand) > 4:
                print('Error: Numbers cannot be more than four digits.')
                return
            if operand == '+' or operand == '-':
                pass
            elif not operand.isdigit():
                print('Error: Numbers must only contain digits.')
                return
        operand1_list.append(operands[0])
        operand2_list.append(operands[2])
        max_operand = 0
        for operand in operands:
            if operand != '+' and operand != '-' and (int(operand)) > max_operand:
                max_operand = int(operand)
        max_len_list.append (len(str(max_operand))+2)
    print(sign_list,operand1_list,operand2_list,max_len_list)
# Actual solving and output
    first_line = ''
    second_line = ''
    sep_line = ''
    solution_line = ''
    for operand,length in zip(operand1_list,max_len_list):
        first_line += ((' ' * (int(length) - len(operand))) + operand + (' '* 4))
    print(first_line.rstrip())
    for operand,sign,length in zip(operand2_list,sign_list,max_len_list):
        second_line += ((sign + (' ' * (int(length) - len(operand) - 1)) + operand +(' '* 4)))
    print(second_line.rstrip())
    for length in max_len_list:
        sep_line += ('-' * int(length)) + (' ' * 4)
    print(sep_line.rstrip())
    for operand1,operand2,length,sign in zip(operand1_list, operand2_list,max_len_list,sign_list):
        if sign == '+':
            solution = str(int(operand1) + int(operand2))
        if sign == '-':
            solution = str(int(operand1) - int(operand2))
        solution_line += ((' ' * (int(length) - len(solution))) + solution + (' '* 4))
    if solution_check == 'True':
        print(solution_line.rstrip())

if __name__ == '__main__':
    arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"],input('Print solution?(True or False): '))