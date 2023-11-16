import os
import hashlib
class Worker:
    NUMBER_RANGE = 10000
    CHUNK = 100

    def __init__(self):
        self.found = False
        self.result = None

    @staticmethod
    def PasswordCreate(inputVar):
        password = hashlib.md5()
        password.update(inputVar.encode("utf-8"))
        return password.hexdigest()

    def seek4Secret(self, start, end, secret):
        for i in range(start, end):
            s = str(i).zfill(len(str(Worker.NUMBER_RANGE)) - 1)
            displayPass = Worker.PasswordCreate(s)
            if displayPass == secret:
                self.result = s
                self.found = True
                return
            print(f"User Password of {i} is: {displayPass}")



def main():
    secret = Worker.PasswordCreate("99")
    print(f"secret is {secret}")
    myworker = Worker()
    # Create Variable for dipslay encoded value.
    for i in range(0, Worker.NUMBER_RANGE, Worker.CHUNK):
        print(f"working on range {i} till {i+Worker.CHUNK}")
        myworker.seek4Secret(i, i+Worker.CHUNK, secret)
        if myworker.found:
            print(f"found {myworker.result}")
            break
    num = os.cpu_count()

    print(num)


if __name__ == "__main__":
    main()
