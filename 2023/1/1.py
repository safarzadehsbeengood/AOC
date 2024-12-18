def digitToString(digit):
    if digit == 0:
        return 'zero'
    if digit == 1:
        return 'one'
    if digit == 2:
        return 'two'
    if digit == 3:
        return 'three'
    if digit == 4:
        return 'four'
    if digit == 5:
        return 'five'
    if digit == 6:
        return 'six'
    if digit == 7: 
        return 'seven'
    if digit == 8:
        return 'eight'
    if digit == 9:
        return 'nine'

def stringToDigit(s):
    s = s.lower()
    if s == 'zero':
        return 0
    if s == 'one':
        return 1
    if s == 'two':
        return 2
    if s == 'three':
        return 3
    if s == 'four':
        return 4
    if s == 'five':
        return 5
    if s == 'six':
        return 6
    if s == 'seven': 
        return 7
    if s == 'eight':
        return 8
    if s == 'nine':
        return 9
    
calibrations = []
with open("input.txt") as input:
    lines = input.read().splitlines()
    first = last = None
    sFirst = sLast = None
    
    for line in lines:
        spelled = {}

        # make a dictionary with the first and last occurrence of all spelled out digits
        for i in range(10):
            sNum = digitToString(i)
            spelled[sNum] = (line.find(sNum), line.rfind(sNum))
        
        firstSpelledIndex = len(line) + 1
        lastSpelledIndex = -1

        # look for the first and last occurring spelled digit
        for sNum, indices in spelled.items():
            if 0 <= indices[0] < firstSpelledIndex:
                firstSpelledIndex = indices[0]
                first = stringToDigit(sNum)
                sFirst = sNum
            if indices[1] > lastSpelledIndex:
                lastSpelledIndex = indices[1]
                last = stringToDigit(sNum)
                sLast = sNum

        for i in range(len(line)):
            if ('0' <= line[i] <= '9') and (i < firstSpelledIndex):
                first = int(line[i])
                break
        for i in range(len(line) - 1, -1, -1):
            if ('0' <= line[i] <= '9') and (i > lastSpelledIndex):
                last = int(line[i])
                break
        
        # print(line.rjust(60) + ' : ' + str(first) + str(last))


        calibrations.append(int(str(first) + str(last)))

print(sum(calibrations))




    

