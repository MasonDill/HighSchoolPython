def get_Tumors(filename, type): #creates the array of tumors
    tumors = []
    txtReader = open(filename, "r")

    for line in txtReader:
        if line[len(line) - 2] == type:
            tumors.append(line.split(','))

    txtReader.close()
    return tumors

def compute_avgs(filename, type): #computes array of averages for specified type of tumor
    tumors = get_Tumors(filename, type)
    averages = [0] * (len(tumors[0]) - 2)  # declares averages array holding all 10 attributes, -2 so that ID and M/B are ignored

    for row in range(0, len(tumors) - 1):  # holds number of rows
        for col in range(0, len(averages)):
            averages[col] += float(tumors[row][col])  # adds together total value of each attribute

    for element in range(0, len(averages)):
        averages[element] /= len(tumors)

    return averages


def classify(filename, m_avgs, b_avgs):
    correct = 0  #keeps track of correct guesses
    guesses = 0  #keeps track of total guesses
    txtReader = open(filename, "r")

    for line in txtReader: #reads in each tumor

        while(line[0:2] == "//"):
            line = txtReader.readline()

        tumor = line.split(",") #puts the tumor into an array

        benign = 0 #keeps track of how many attributes are closer to benign

        for attribute in range(0, len(tumor) -2): #finds how many attributes it has in common with a benign tumor
            if abs(float(tumor[attribute]) - b_avgs[attribute]) < abs(float(tumor[attribute]) - m_avgs[attribute]): #attribute is closer to benign - if equally between b and m assumes malignant, assume worst case scenario
                benign +=1

        if benign > 5 and line[len(line) -2] == "B": #benign guess was correct - guesses begign only if it has a mojority benign attributes
            correct +=1

        elif benign <= 5 and line[len(line) -2] == "M": #malignant guess was correct  - guesses malignant if has a mojority malignant attributes or is a split between the two, always assume worst case scenario
            correct +=1

        guesses +=1
    txtReader.close()

    print(correct, "correct guesses out of", guesses,"- %"+ str(correct/guesses*100))

def main():
    m_avgs = compute_avgs("trainingDataset.txt", "M")
    b_avgs=  compute_avgs("trainingDataset.txt", "B")

    classify("testingDataset.txt", m_avgs, b_avgs)
main()