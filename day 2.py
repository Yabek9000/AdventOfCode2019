
def Computer(noun,verb ):
    instruction_pointer = 0
    Intcode[1] = str(noun)
    Intcode[2] = str(verb)

    while True:

        Opcode = int(Intcode[instruction_pointer])

        if Opcode == 99:
            break

        elif Opcode == 1:
            Parameter1 = int(Intcode[int(Intcode[instruction_pointer + 1])])
            Parameter2 = int(Intcode[int(Intcode[instruction_pointer + 2])])
            Destination_Parameter = int(Intcode[instruction_pointer + 3])
            
            Intcode[Destination_Parameter] = str(Parameter1 + Parameter2)

        elif Opcode == 2:
            Parameter1 = int(Intcode[int(Intcode[instruction_pointer + 1])])
            Parameter2 = int(Intcode[int(Intcode[instruction_pointer + 2])])
            Destination_Parameter = int(Intcode[instruction_pointer + 3])
            
            Intcode[Destination_Parameter] = str(Parameter1 * Parameter2)
            
        instruction_pointer += 4
    return Intcode[0]




target_output = 19690720

for noun in range(100):
    for verb in range(100):
        file = open("data2","r")
        filelines = file.readlines()

        Intcode = []
        for number in filelines:
            number = number.split(",")
            Intcode.extend(number)
        
        output = Computer(noun, verb)

        # Check if the output matches the target
        if output == str(target_output):
            print(100 * noun + verb)
