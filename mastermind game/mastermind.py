import random
CODE_LEN = 4
COLORS = ["R","B","G","Y","O"]
tries = 10
def generate_code():
    code = []
    for _ in range(CODE_LEN):
        color = random.choice(COLORS)
        code.append(color)
    return code
def guess_code():
    guess = input("guess the code: ").upper().split(" ")
    while True:
        if len(guess) != CODE_LEN:
            print(f"enter the {CODE_LEN} length string")
            continue
        for i in guess:
            if i not in COLORS:
                print("invalid color")
                break
        else:
            break
    return guess

def check_code(code,guess):
    correct_pos = 0
    incorrect_pos = 0
    color_dict = {}
    for color in code:
        if color not in  color_dict:
            color_dict[color] = 0
        color_dict[color] +=1
   
    for guess_color,code_color in zip(guess,code):
        if guess_color == code_color:
            correct_pos +=1
            color_dict[guess_color] -= 1
        
    for guess_color,code_color in zip(guess,code):
        if guess_color in color_dict and color_dict[guess_color] > 0:
            incorrect_pos +=1
            color_dict[guess_color] -= 1

    return correct_pos,incorrect_pos

def main():
    print("welcome to mastermind. Find the correct order of colors to win the game")
    print(f"The color you are about to predict are between {COLORS}")
    code = generate_code()
    print(code)
    for i in range(0,tries +1):
        guess = guess_code()

        correct_pos,incorrect_pos = check_code(code, guess)
        print(color_dict)
        if correct_pos == CODE_LEN:
            print("CONGRATULATIONS!!!")
            print(f"you find the code in {i} attemps ")
            break
        else:
            print(f"correct positions: {correct_pos}| incorrect position: {incorrect_pos}")

    else:
        
        print("you ran out of tries, the code is: ", *code)    

if __name__ == "__main__":
    main()

