employees = [
    (101, "Alice", "HR", "Absent"),
    (102, "Bob", "IT", "Absent"),
    (103, "Charlie", "Finance", "Absent"),
    (104, "David", "Marketing", "Absent"),
]

while True:
    print("\n1. Mark Attendance\n2. Search Attendance\n3. Display Summary\n4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        emp_id = int(input("Enter Employee ID: "))
        if any(emp_id == emp[0] for emp in employees):
            status = input("Enter status (Present/Absent): ")
        
        
            if status in ["Present", "Absent"]:
                employees = [(id, name, dept, status if id == emp_id else att) for id, name, dept, att in employees]
                print(f"Attendance updated for Employee ID {emp_id}: {status}")
            else:
                print("Invalid status! Use 'Present' or 'Absent'.")
        else:
            print("Id not found")

            
    elif choice == "2":
        emp_id = int(input("Enter Employee ID to search: "))
        found = False
        for emp in employees:
            if emp[0] == emp_id:
                print(f"Employee_Name: {emp[1]}, Department: {emp[2]}, Attendance: {emp[3]}")
                found = True
                break
        if not found:
            print("Employee ID not found.")

    elif choice == "3":
        print("\nAttendance Summary:")
        for emp in employees:
            print(f"ID: {emp[0]}, Name: {emp[1]}, Department: {emp[2]}, Attendance: {emp[3]}")

    elif choice == "4":
        print("Exited!")
        break

    else:
        print("Invalid choice! Please enter a number between 1-4.")
