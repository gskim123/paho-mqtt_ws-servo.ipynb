def Func_CallBack(c):
    print("File Length : ", c)
    
def File_Len(filepath, callback):
    with open(filepath,"r") as i:
        file_length = len(i.read())
        callback(file_length)

if __name__ == '__main__':
    File_Len("random.txt", Func_CallBack)