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
            "status": "Pending",
            "requisition_id": f"{staff_id}{str(self.counter)[-3:]}"
        }
        if total <= 500:
            req["status"] = "Approved"
            self.approved += 1
        else:
            req["status"] = "Pending"
            self.pending += 1

        self.requisitions.append(req)
        return req

    def approve_requisition(self, requisition_id):

        for req in self.requisitions:
            if req["requisition_id"] == requisition_id:

                if req["status"] == "Pending":
                    req["status"] = "Approved"
                    self.approved += 1
                    self.pending -= 1
                    return True

        return False

    def reject_requisition(self, requisition_id):

        for req in self.requisitions:
            if req["requisition_id"] == requisition_id:

                if req["status"] == "Pending":
                    req["status"] = "Rejected"
                    self.rejected += 1
                    self.pending -= 1
                    return True

        return False

    def display_requisitions(self):

        print("\n===== Requisition List =====")

        for req in self.requisitions:
            print("-------------------------")
            print("Date:", req["date"])
            print("staff ID:", req["staff_id"])
            print("Staff Name:", req["name"])
            print("Items:", req["items"])
            print("Total:", req["total"])
            print("Requisition ID:", req["requisition_id"])
            print("Status:", req["status"])

    def display_statistics(self):

        print("===== Statistics =====")
        print("Total Requisitions:", len(self.requisitions))
        print("Approved:", self.approved)
        print("Pending:", self.pending)
        print("Rejected:", self.rejected)


system = RequisitionSystem()

items1 = [
    {"name": "laptop", "price": 450},
    {"name": "mouse", "price": 30}
]
items2 = [
    {"name": "Monitor", "price": 600}
]

system.add_requisition("20/11/2026", "A01", "Apurba_Paul", items1)
system.add_requisition("20/11/2026", "A2", "Jafor", items2)

system.display_requisitions()
system.display_statistics()