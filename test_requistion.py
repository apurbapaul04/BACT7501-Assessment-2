from requisition_system import RequisitionSystem

system = RequisitionSystem()

while True:

    print("\n===== Requisition System =====")
    print("1. Create Requisition")
    print("2. Manager Response")
    print("3. Display Requisitions")
    print("4. Display Statistics")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":

        date = input("Enter date: ")
        staff_id = input("Enter staff ID: ")
        name = input("Enter staff name: ")

        items = []

        while True:

            item_name = input("Enter item name: ")
            price = float(input("Enter price: "))

            items.append({
                "name": item_name,
                "price": price
            })

            more = input("Add more items? (yes/no): ")

            if more.lower() != "yes":
                break

        req = system.add_requisition(
            date, staff_id, name, items
        )

        print("Requisition ID:", req["requisition_id"])
        print("Total: $", req["total"])
        print("Status:", req["status"])

    elif choice == "2":

        req_id = input("Enter requisition ID: ")
        decision = input("Approve or reject: ").lower()

        if decision == "approve":
            system.approve_requisition(req_id)

        elif decision == "reject":
            system.reject_requisition(req_id)

    elif choice == "3":

        system.display_requisitions()

    elif choice == "4":

        system.display_statistics()

    elif choice == "5":

        print("Program closed.")
        break

    else:

        print("Invalid choice.")