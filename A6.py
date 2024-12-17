class Time:
    def __init__(self, hrs, mins, secs):
        self.hrs = hrs
        self.mins = mins
        self.secs = secs
        self.normalize_time()

    def normalize_time(self):
        if self.secs >= 60:
            self.mins += self.secs // 60
            self.secs %= 60
        elif self.secs < 0:
            self.mins -= (-self.secs // 60) + 1
            self.secs = 60 + (self.secs % 60)

        if self.mins >= 60:
            self.hrs += self.mins // 60
            self.mins %= 60
        elif self.mins < 0:
            self.hrs -= (-self.mins // 60) + 1
            self.mins = 60 + (self.mins % 60)

        if self.hrs < 0:
            self.hrs, self.mins, self.secs = 0, 0, 0

    def display(self):
        return f"{self.hrs} Hr(s) {self.mins} Min(s) {self.secs} Sec(s)"

    def __add__(self, other):
        return Time(self.hrs + other.hrs, self.mins + other.mins, self.secs + other.secs)

    def __sub__(self, other):
        return Time(self.hrs - other.hrs, self.mins - other.mins, self.secs - other.secs)

    def __mul__(self, multiplier):
        total_seconds = (self.hrs * 3600 + self.mins * 60 + self.secs) * multiplier
        return Time(total_seconds // 3600, (total_seconds % 3600) // 60, total_seconds % 60)


    def from_input():
        while True:
            hrs = int(input("Enter hours (0-23): "))
            if hrs < 0 or hrs > 23:
                print("Error: Hours must be between 0 and 23.")
                
            mins = int(input("Enter minutes (0-59): "))
            if mins < 0 or mins > 59:
                print(" Minutes must be between 0 and 59.")
          
            secs = int(input("Enter seconds (0-59): "))
            if secs < 0 or secs > 59:
                print("Error: Seconds must be between 0 and 59.")
            
            return Time(hrs, mins, secs)

# Example usage
print("Input Time 1:")
p1 = Time.from_input()

print("Input Time 2:")
p2 = Time.from_input()

multiplier = int(input("Enter Multiplier for Time 1: "))

ADD = p1 + p2
SUB = p2 - p1
MUL = p1 * multiplier

print(f"ADD(+): {ADD.display()}")
print(f"SUB(-): {SUB.display()}")
print(f"MUL(*): {MUL.display()}")
