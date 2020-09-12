
if __name__ == "__main__":
    print("測試".encode('utf-8'))
    print("測試".encode('unicode-escape'))
    # unknown encoding: unicode
    # print("測試".encode('unicode'))
    print(b'\xe6\xb8\xac\xe8\xa9\xa6'.decode('utf-8'))
