
    

class Buzzer:
    def __init__(self, frequency = 100):
        self.frequency = frequency
        self.cycles = 0

    def ring(self, cycles = 1):
        self.cycles = cycles
        for i in range(self.cycles):
            print("BEEP!")
        self.cycles = 0

def main():
    buzzer = Buzzer()
    buzzer.ring(2)

if __name__ == '__main__':
    main()    