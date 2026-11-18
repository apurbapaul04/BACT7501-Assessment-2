class RequisitionSystem:

    def __init__(self):
        self.requisitions = []
        self.requisition_counter = 10000

        self.total_submitted = 0
        self.approved = 0
        self.pending = 0
        self.not_approved = 0