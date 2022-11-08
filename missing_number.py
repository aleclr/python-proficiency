n = int(input('Informe o valor de N: '))
seq = input('Informe a sequência numerada de inteiros: ')
print(type(n), type(seq))

seq_array = seq.split(' ')
seq_array_int = []
for number in seq_array:
    number = int(number)
    seq_array_int.append(number)

count = 1
array_base = []
missing_number = 0
while count <= n:
    print(count)
    ###########
    array_base.append(count)
    if array_base[count - 1] not in seq_array_int:
        missing_number = array_base[count - 1]
        break
    ###########
    count += 1

print(array_base)
print(seq_array_int)
print(missing_number)