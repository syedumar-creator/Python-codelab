def search_word():
    word="Python"
    line=1
    with open("Sample.txt","r")as f:
        while True:
            data=f.readline()
            if(word in data != -1):
                print("Found at ",line)
                return
            line+=1
    return -1
search_word()