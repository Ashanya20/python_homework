# Task 1: Hello function
def hello():
    return "Hello!"

# Task 2: Greet function
def greet(name):
    return f"Hello, {name}!"

# Task 3: Calculator function
def calc(value1, value2, operation="multiply"):
    try:
        if operation == "add":
            return value1 + value2
        elif operation == "subtract":
            return value1 - value2
        elif operation == "multiply":
            return value1 * value2
        elif operation == "divide":
            return value1 / value2
        elif operation == "modulo":
            return value1 % value2
        elif operation == "int_divide":
            return value1 // value2
        elif operation == "power":
            return value1 ** value2
    except ZeroDivisionError:
        return "You can't divide by 0!"
    except TypeError:
        if operation == "multiply":
            return "You can't multiply those values!"
        else:
            return f"You can't {operation} those values!"

# Calculator function with match-case
# def calc(value1, value2, operation="multiply"):
#     try:
#         match operation:
#             case "add":
#                 return value1 + value2
#             case "subtract":
#                 return value1 - value2
#             case "multiply":
#                 return value1 * value2
#             case "divide":
#                 return value1 / value2
#             case "modulo":
#                 return value1 % value2
#             case "int_divide":
#                 return value1 // value2
#             case "power":
#                 return value1 ** value2
#             case _:
#                 return "Invalid operation"
#     except ZeroDivisionError:
#         return "You can't divide by 0!"
#     except TypeError:
#         return "You can't multiply those values!"

# Task 4: Data Type Conversion
def data_type_conversion(value, type):
    try:
        if type == "float":
            return float(value)
        elif type == "str":
            return str(value)
        elif type == "int":
            return int(value)
    except ValueError:
        return f"You can't convert {value} into a {type}."

# Task 5: Grading System
def grade(*args):
    try:
        average = sum(args) / len(args)
        
        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"
    except (TypeError, ZeroDivisionError):
        return "Invalid data was provided."

# Task 6: Repeat with for loop
def repeat(string, count):
    result = ""
    for i in range(count):
        result = result + string
    return result

# Task 7: Student Scores
def student_scores(option, **kwargs):
    if option == "best":
        best_student = None
        best_score = -1
        for student, score in kwargs.items():
            if score > best_score:
                best_score = score
                best_student = student
        return best_student
    
    elif option == "mean":
        scores = kwargs.values()
        total = sum(scores)
        count = len(scores)
        return total / count

# Task 8: Titleize
def titleize(title):
    little_words = ["a", "on", "an", "the", "of", "and", "is", "in"]
    words = title.split()
    result_words = []
    
    for i, word in enumerate(words):
        if i == 0 or i == len(words) - 1:
            result_words.append(word.capitalize())
        elif word.lower() in little_words:
            result_words.append(word.lower())
        else:
            result_words.append(word.capitalize())
    
    return " ".join(result_words)

# Task 9: Hangman
def hangman(secret, guess):
    result = ""
    for char in secret:
        if char in guess:
            result = result + char
        else:
            result = result + "_"
    return result

# Task 10: Pig Latin
def pig_latin(sentence):
    vowels = "aeiou"
    result = []
    
    for word in sentence.split():
        if word.startswith("qu"):
            result.append(word[2:] + "quay")
        else:
            consonant_end = 0
            while consonant_end < len(word):
                if word[consonant_end] == 'q' and consonant_end + 1 < len(word) and word[consonant_end + 1] == 'u':
                    consonant_end += 2
                elif word[consonant_end] in vowels:
                    break
                else:
                    consonant_end += 1
            
            result.append(word[consonant_end:] + word[:consonant_end] + "ay")
    
    return " ".join(result)

# Testing
# print(hello())
# print(greet("Alice"))

# print(calc(10, 5, "add"))
# print(calc(8, 5, "subtract"))
# print(calc(3, 5, "multiply"))
# print(calc(15, 5, "divide"))
# print(calc(11, 3, "modulo"))
# print(calc(12, 3, "int_divide"))
# print(calc(3, 3, "power"))
# print(calc(7, 0, "divide"))
# print(calc("a", "b", "multiply"))

# print(data_type_conversion("3.14", "float"))
# print(data_type_conversion(456, "str"))
# print(data_type_conversion("123", "int"))
# print(data_type_conversion("hello", "int"))
# print(data_type_conversion("abc", "float"))

# print(grade(95, 85, 90))
# print(grade(85, 75, 80))
# print(grade(75, 65, 70))
# print(grade(65, 55.9, 60))
# print(grade(50, 40, 30))
# print(grade(100.5))
# print(grade(85, "one", 75))

# print(repeat("hi", 4))
# print(repeat("!", 3))

# print(student_scores("best", Alice=95, Bob=87, Kate=92))
# print(student_scores("mean", John=78, Jane=88, Jack=98))

# print(titleize("the great day of a summer in.."))

# print(hangman("mississippi", "si"))

# print(pig_latin("square"))