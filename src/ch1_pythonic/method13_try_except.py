def func():
    try:
        print("try")
        raise Exception("try failed.")
    except Exception as e:
        raise ValueError("Wrong inputs") from e
    else:
        print("else")
        raise Exception("else failed.")
    finally:
        print("finally")
        # return "finally"


if __name__ == "__main__":
    try:
        print("func")
        print(func())
    except Exception as e:
        print(e)
