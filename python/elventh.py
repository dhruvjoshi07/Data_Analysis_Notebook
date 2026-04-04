class Student:
    # Class Variable (Sabhi students ke liye same rahega)
    college_name = "Chandigarh University"

    def __init__(self, name, marks):
        self.name = name   # Instance Variable
        self.marks = marks # Instance Variable

    # 1. Instance Method
    # Isse 'self' chahiye kyunki har student ka naam aur marks alag hote hain.
    def display_info(self):
        print(f"Name: {self.name}, Marks: {self.marks}, College: {self.college_name}")

    # 2. Class Method
    # Isse 'cls' chahiye kyunki humein poori class ka common data (college name) change karna hai.
    @classmethod
    def change_college(cls, new_name):
        cls.college_name = new_name
        print(f"College name changed to: {cls.college_name}")

    # 3. Static Method
    # Isse na 'self' chahiye na 'cls'. Yeh bas ek utility tool hai 
    # jo sirf percentage calculate karke deta hai (generic math).
    @staticmethod
    def calculate_percentage(obtained, total):
        return (obtained / total) * 100

# --- Execution ---

# Student objects banaye
s1 = Student("Dhruv", 85)
s2 = Student("Arjun", 92)

# Instance Method call kiya (Object ka data dikhane ke liye)
s1.display_info()

# Static Method call kiya (Bina object banaye bhi calculation kar sakte hain)
result = Student.calculate_percentage(85, 100)
print(f"Percentage: {result}%")

# Class Method call kiya (Poori class ke liye college badal diya)
Student.change_college("CU Mohali")

# Ab check karte hain kya change reflect hua?
s1.display_info()
s2.display_info()