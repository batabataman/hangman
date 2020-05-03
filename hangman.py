import random
def hangman():
    word_list = ["dog", "cat", "bird","fish"]
    index = random.randint(0,len(word_list) - 1)
    print(index)
    word = word_list[index]
    wrong = 0
    stages = ["",
              "____________          ",
              "|                     ",
              "|          |          ",
              "|          O          ",
              "|         /|\         ",
              "|         / \         ",
              "|                     "
              ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("ハングマンヘようこそ")

    while wrong < len(stages) - 1:
        print("\n")
        msg = "1文字を予想してね"
        char = input(msg)
        #print(stages[wrong])
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
            print(wrong)
        print(" ".join(board))
        e = wrong + 1
        print("e={}".format(str(e)))
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("あなたの勝ち")
            print(" ".join(board))
            win = True
            break

    if not win:
        print("\n".join(stages[0: wrong + 1]))
        print("あなたの敗け。正解は{}.".format(word))

hangman()
    
