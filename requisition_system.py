
class RequisitionSystem:

    def __init__(self):
        self.requisitions = []
        self.counter = 10000

        self.approved = 0
        self.pending = 0
        self.rejected = 0

    def add_requisition(self, date, staff_id, name, items):

        total = sum(item["price"] for item in items)

        self.counter += 1

        req = {
            "date": date,
            "staff_id": staff_id,
            "name": name,
            "items": items,
            "total": total,
            "requisition_id": str(self.counter),
            "status": "Pending",
            "approval_reference": "Not available"
        }

        if total <= 500:
            req["status"] = "Approved"
            req["approval_reference"] = (
                staff_id + str(self.counter)[-3:]
            )
            self.approved += 1

        else:
            self.pending += 1

        self.requisitions.append(req)

        return req

    def approve_requisition(self, requisition_id):

        for req in self.requisitions:

            if req["requisition_id"] == requisition_id:

                if req["status"] == "Pending":

                    req["status"] = "Approved"

                    req["approval_reference"] = (
                        req["staff_id"] + requisition_id[-3:]
                    )

                    self.approved += 1
                    self.pending -= 1

                    return True

        return False

    def reject_requisition(self, requisition_id):

        for req in self.requisitions:

            if req["requisition_id"] == requisition_id:

                if req["status"] == "Pending":

                    req["status"] = "Not approved"

                    self.rejected += 1
                    self.pending -= 1

                    return True

        return False

    def display_requisitions(self):

        print("\n===== Requisition List =====")

        for req in self.requisitions:

            print("\nDate:", req["date"])
            print("Requisition ID:", req["requisition_id"])
            print("Staff ID:", req["staff_id"])
            print("Staff Name:", req["name"])
            print("Total: $" + str(req["total"]))
            print("Status:", req["status"])
            print("Approval Reference Number:",
                req["approval_reference"])

    def display_statistics(self):

        print("\n===== Statistics =====")

        print("Total Requisitions:", len(self.requisitions))
        print("Approved:", self.approved)
        print("Pending:", self.pending)
        print("Not approved:", self.rejected)


system = RequisitionSystem()

items1 = [
    {"name": "Laptop", "price": 450}
]

items2 = [
    {"name": "Monitor", "price": 1000}
]

items3 = [
    {"name": "Computer", "price": 3500}
]

items4 = [
    {"name": "Keyboard", "price": 490}
]


system.add_requisition("03/04/2024", "FN19", "John Paul", items1)

system.add_requisition("05/04/2024", "FN20", "Tracy Brown", items2)

system.add_requisition("07/05/2024", "FN15", "Emma Wellington", items3)

system.add_requisition("03/05/2024", "FN02", "Catlin White", items4)

system.reject_requisition("10003")
system.display_requisitions()
system.display_statistics()
