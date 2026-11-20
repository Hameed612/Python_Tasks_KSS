# Create Result class
class Result:

    # Use default argument for optional third subject
    def calculate(self, m1, m2, m3=None):

        if m3 is None:
            total = m1 + m2
            average = total / 2
        else:
            total = m1 + m2 + m3
            average = total / 3

        print("Total Marks:", total)
        print("Average Marks:", average)


# Create object
r1 = Result()

# Calculate using two subjects
print("Two Subjects:")
r1.calculate(80, 90)

# Calculate using three subjects
print("Three Subjects:")
r1.calculate(80, 90, 70)