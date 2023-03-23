#Basic recursive function example


def EvenNums(num):
    print(num)
    if num == 2:
        return 2
    else: return EvenNums(num-2)

EvenNums(10)    
