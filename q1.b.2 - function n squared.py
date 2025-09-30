

def function_n_squared(number):
    n = len(number)
    for i in range(n):
        print("Iteration: " + str(i+1)) 
        for j in range(n):
            result = number[i] + number[j]
            print(result)
    return result

function_n_squared('ab')


