def parse_input(path):
    # Read file and split into lines
    with open(path, 'r') as file:
        result = file.read().splitlines()
    # Optional: Remove any empty lines if needed
    return [line.split() for line in result if line.strip()]


def main():
    input_path = 'input.txt'
    input_lines = parse_input(input_path)
    solution=0
    for line in input_lines:
        safety=check_for_safety(line)
        if safety:
            solution+=1
        else:
            for i in range(0,len(line)):
                newline=line[:i]+line[i+1:]
                safety=check_for_safety(newline)
                if safety:
                    solution+=1
                    break
    print(solution)


def check_for_safety(line):
    line=[int(x) for x in line]
    safe=True
    #make sure the line is all ascending or descending
    if sorted(line)==line or sorted(line,reverse=True)==line:
        #make sure the line rises or falls between 1 and 3
        for i in range(len(line)):
            if i!=0:
                if line[i]==line[i-1]:
                    print(f"{line[i]} and {line[i-1]} match")
                    safe=False
                elif abs(int(line[i])-int(line[i-1]))>3:
                    print(f"too big of a jump from {line[i-1]} to {line[i]}")
                    safe=False
    else:
        print(f"{line} not all ascending/descending")
        safe=False
    return safe


# Run the main function
if __name__ == '__main__':
    main()
