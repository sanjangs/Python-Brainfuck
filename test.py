from brainfuck import Brainfuck

t1_code = "++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++."

print('-' * 125)
print("Test 1: Hello World Program")
print("Code:", t1_code)
print("Result: ", end='')

Brainfuck(t1_code)
print('-' * 125)
