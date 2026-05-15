complaint_words = [
    "bad",
    "terrible",
    "refund",
    "slow",
    "late",
    "issue",
    "problem",
    "horrible",
    "worst"
]

def detect_complaint(text):

    text = text.lower()

    for word in complaint_words:

        if word in text:
            return "Complaint"

    return "No Complaint"