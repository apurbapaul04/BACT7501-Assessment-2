from requisition_system import RequisitionSystem
system = RequisitionSystem()

items1 = [
    {"name": "Pens", "price": 150},
    {"name": "Notebooks", "price": 300}
]
system.add_requisition("03/04/2024", "FN19", "John Paul", items1)

items2 = [
    {"name": "Laptop", "price": 1000}
]
system.add_requisition("05/04/2024", "FN20", "Tracy Brown", items2)

items3 = [
    {"name": "Printer", "price": 2500},
    {"name": "Toner", "price": 1000}
]
system.add_requisition("07/05/2024", "FN15", "Emma Wellington", items3)

items4 = [
    {"name": "Desk lamp", "price": 90},
    {"name": "Chair", "price": 400}
]
system.add_requisition("03/05/2024", "FN02", "Catlin White", items4)

items5 = [
    {"name": "Keyboard", "price": 200},
    {"name": "Mouse", "price": 350}
]
system.add_requisition("10/05/2024", "FN17", "Kabir Khan", items5)

items6 = [
    {"name": "Stapler", "price": 10.50},
    {"name": "Tape", "price": 15},
    {"name": "Sticker", "price": 5}
]
system.add_requisition("12/05/2024", "FN11", "Nibas Mohanta", items6)


print("\nBefore manager responses")
system.display_requisitions()
system.display_statistics()


print("\nManager responses")

system.reject_requisition("10003")
system.approve_requisition("10002")
system.approve_requisition("10005")


print("\nAfter manager responses")
system.display_requisitions()
system.display_statistics()