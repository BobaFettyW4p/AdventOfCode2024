def get_data():
    with open('input.txt','r') as f:
        return f.read()

def process_data(dataset):
    dataset=dataset.split("\n")
    processed_dataset=[]
    for line in dataset:
        processed_dataset.append(line.split("   "))
    leftSide =[]
    rightSide=[]
    for line in processed_dataset:
        if len(line)==2:
            leftSide.append(line[0])
            rightSide.append(line[1])
    leftSide.sort()
    rightSide.sort()
    return leftSide,rightSide

def compare_datasets(leftSide,rightSide):
    answer=0
    for i in range(0,len(leftSide)):
        answer+=abs(int(leftSide[i])-int(rightSide[i]))
    return answer
    

dataset=get_data()
leftSide,rightSide=process_data(dataset)
answer=compare_datasets(leftSide,rightSide)
print(answer) #1646452
