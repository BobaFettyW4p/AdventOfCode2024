import re

def read_data(filename):
    with open(filename, "r") as f:
        data=f.readlines()
    return data

def test_for_valid_game(line):
    game_number=re.findall(r"Game (\d+)",line)
    blue_results=re.findall(r"(\d+) blue",line)
    red_results=re.findall(r"(\d+) red",line)
    green_results=re.findall(r"(\d+) green",line)
    for result in blue_results:
        if int(result)>TOTAL_CUBES["blue"]:
            return False
    for result in red_results:
        if int(result)>TOTAL_CUBES["red"]:
            return False
    for result in green_results:
        if int(result)>TOTAL_CUBES["green"]:
            return False
    return True
    
def main(data):
    sum_of_ids=0
    for line in data:
        print(f"processing {line}")
        if test_for_valid_game(line):
            match=re.search(r"^Game (\d+)",line)
            sum_of_ids+=int(match.group(1))
            print(f"game {match.group(1)} is a match. cumulative sum is {sum_of_ids}")
        #else:
            #print(f"game is not valid. Continuing...")
    return sum_of_ids

def game_test(data):
    for line in data:
        match=re.search(r"^Game (\d+)",line)
        print(match.group(1))

if __name__=='__main__':
    TOTAL_CUBES={"red":12,"green":13,"blue":14}
    data=read_data('Day2/input.txt')
    sum_of_ids=main(data)
    print(sum_of_ids) # 2207
    #matches=game_test(data)
    #print(matches)