# Hi 3 -> HiHiHi

def make_repeter_of(n):
    def repeter(string):
        assert type(string) == str, "You can use just strings"
        return string * n
    return repeter

def run():
    repeat_5 = make_repeter_of(5)
    print(repeat_5("Word"))


if __name__ == '__main__':
    run()

