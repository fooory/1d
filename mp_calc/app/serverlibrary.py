

def merge(array, p, q, r, byfunc=None):
    nleft = q - p + 1
    nright = r - q

    left_array = array[p:q+1]
    right_array = array[q + 1: r+1]

    left = 0
    right = 0
    destination = p

    while left < nleft and right < nright:
        if byfunc is None:
            if left_array[left] <= right_array[right]:
                array[destination] = left_array[left]
                left += 1
            else:
                array[destination] = right_array[right]
                right += 1
        else:
            if byfunc(left_array[left]) <= byfunc(right_array[right]):
                array[destination] = left_array[left]
                left += 1
            else:
                array[destination] = right_array[right]
                right += 1
        destination += 1

    while left < nleft:
        array[destination] = left_array[left]
        left += 1
        destination += 1

    while right < nright:
        array[destination] = right_array[right]
        right += 1
        destination += 1

def mergesort_recursive(array, p, r, byfunc=None):
    if p < r:
        q = (p + r) // 2
        mergesort_recursive(array, p, q, byfunc)
        mergesort_recursive(array, q + 1, r, byfunc)
        merge(array, p, q, r, byfunc)

def mergesort(array, byfunc=None):
    mergesort_recursive(array, 0, len(array) - 1, byfunc)

#def mergesort(array, byfunc=None):
  #pass

class Stack:
  def __init__(self):
    self.__items = []
        
  def push(self, item):
    self.__items.append(item)

  def pop(self):
    return self.__items.pop() if not self.is_empty else None

  def peek(self):
    return self.__items[-1]

  @property
  def is_empty(self):
    return self.__items == []

  @property
  def size(self):
    return len(self.__items)


class EvaluateExpression:
  valid_char = '0123456789+-*/() '
  
  def __init__(self, string=""):
    self._expr = string
    pass

  @property
  def expression(self):
    return self._expr

  @expression.setter
  def expression(self, new_expr):
    if all( i in self.valid_char for i in new_expr):
      self._expr = new_expr
    else:
      self._expr = "" #just create a string
    pass

  def insert_space(self):
    valid_operation = '+-*/()'
    dummy = []

    for i in range(len(self._expr)):
      dummy.append(self._expr[i])
    for i in range(len(dummy)):
      if dummy[i] in valid_operation:
        dummy[i] = " " + dummy[i] + " " #adding of spacing at front and back
    spaced_str = "".join(map(str, dummy))
    return spaced_str

  def process_operator(self, operand_stack, operator_stack):
    
    first_out = operand_stack.pop()
    second_out = operand_stack.pop()
    operator_out = operator_stack.pop()

    result = None

    if operator_out == '+':
      result = second_out + first_out
    if operator_out == '-':
      result = second_out - first_out
    if operator_out == '*':
      result = second_out * first_out
    if operator_out == '/':
      result = second_out // first_out
    
    operand_stack.push(result)

  def evaluate(self):
    #MAKE STACK 
    operand_stack = Stack()
    operator_stack = Stack()

    expr = self.insert_space()
    tokens = expr.split() #split via empty space

    for token in tokens:
      if token.isdigit():
        operand_stack.push(int(token)) #important, cuz we feed in a string since expr is a string variable
      elif token in '+-':
        while not operator_stack.is_empty and operator_stack.peek() in '+-*/':
          self.process_operator(operand_stack, operator_stack)
        operator_stack.push(token)
      elif token in '*/':
        while not operator_stack.is_empty and operator_stack.peek() in '*/':
          self.process_operator(operand_stack, operator_stack)
        operator_stack.push(token)
      elif token == '(':
        operator_stack.push(token)
      elif token == ')':
        while operator_stack.peek() != '(':
          self.process_operator(operand_stack, operator_stack)
        operator_stack.pop()

    while not operator_stack.is_empty:
      self.process_operator(operand_stack, operator_stack)
    return operand_stack.pop()


def get_smallest_three(challenge):
  records = challenge.records
  times = [r for r in records]
  mergesort(times, lambda x: x.elapsed_time)
  return times[:3]





