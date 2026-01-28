import csv

# -------------------------------
# TEXT FILE OPERATIONS
# -------------------------------

try:
    # 1. Create text file & 2. Write user data into file
    with open("userdata.txt", "w") as file:
        name = input("Enter your name: ")
        age = input("Enter your age: ")
        file.write(f"Name: {name}\n")
        file.write(f"Age: {age}\n")

    print("Data written to file successfully.")

    # 3. Read file contents
    with open("userdata.txt", "r") as file:
        print("\nFile Contents:")
        print(file.read())

    # 4. Append data to file
    with open("userdata.txt", "a") as file:
        city = input("Enter your city: ")
        file.write(f"City: {city}\n")

    print("\nData appended successfully.")

    # Read again after append
    with open("userdata.txt", "r") as file:
        print("\nUpdated File Contents:")
        print(file.read())

except FileNotFoundError:
    print("File not found!")
except IOError:
    print("File operation error!")
except Exception as e:
    print("Unexpected error:", e)

# -------------------------------
# CSV FILE OPERATIONS
# -------------------------------

try:
    # 6. Create CSV file & 7. Write multiple rows
    with open("students.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["ID", "Name", "Branch", "CGPA"])
        writer.writerow([101, "Manoj", "ECE", 8.6])
        writer.writerow([102, "Rahul", "CSE", 8.4])
        writer.writerow([103, "Anita", "EEE", 8.2])

    print("\nCSV file created and data written.")

    # 8. Read CSV data
    with open("students.csv", "r") as csvfile:
        reader = csv.reader(csvfile)
        print("\nCSV File Contents:")
        for row in reader:
            print(row)

except Exception as e:
    print("CSV file error:", e)

# 9. Files are closed automatically using 'with' statement
