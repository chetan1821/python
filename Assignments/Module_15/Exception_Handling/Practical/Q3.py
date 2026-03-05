# File handling with finally block

try:
    f = open("sample.txt", "r")
    data = f.read()
    print(data)

except FileNotFoundError:
    print("Error: File does not exist")

except Exception as e:
    print("Error:", e)

finally:
    try:
        f.close()
        print("File closed successfully")
    except:
        print("File was not opened")