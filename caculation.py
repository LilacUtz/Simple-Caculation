def add(n1, n2):
  return n1 + n2
 
def subtract(n1, n2):
  return n1 - n2
 
def multiply(n1, n2):
  return n1 * n2
 
def divide(n1, n2):
  return n1 / n2
 
operation = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}
def caculator():
    num_1 = float(input("Please enter first number: "))
    for i in operation:
       print(i)
    should_continue = True
    while should_continue:
        operation_symbol = input("please choose operation form the line above: ")
        num_2 = float(input("Please enter the next number: "))
        caculation = operation[operation_symbol]
        result = caculation(num_1, num_2)
        print(f"{num_1} {operation_symbol} {num_2} = {result}")

        if input(f"Type 'y' to continue with {result} or 'n' to start new: ") == 'y':
          num_1 = result
        else:
          should_continue = False
          caculator()

caculator()