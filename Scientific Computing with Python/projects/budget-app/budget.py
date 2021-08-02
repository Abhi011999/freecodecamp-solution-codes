class Category:
    def __init__(self, category):
        self.ledger = []
        self.amount = 0
        self.category = category

    def check_funds(self, amount):
        return self.amount >= amount

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})
        self.amount += amount

    def withdraw(self, amount, description=""):
        if self.check_funds(amount) == True:
            self.amount -= amount
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:
            return False

    def get_balance(self):
        return self.amount

    def get_withdrawals(self):
        return sum(
            transaction["amount"]
            for transaction in self.ledger
            if transaction["amount"] < 0
        )

    def transfer(self, amount, category):
        if self.check_funds(amount) == True:
            self.amount -= amount
            self.ledger.append(
                {"amount": -amount, "description": "Transfer to " + category.category}
            )
            category.ledger.append(
                {"amount": amount, "description": "Transfer from " + self.category}
            )
            return True
        else:
            return False

    def __str__(self):
        result = "*************Food*************" + "\n"
        for transaction in self.ledger:
            amount = 0
            description = ""
            for key, value in transaction.items():
                if key == "amount":
                    amount = value
                elif key == "description":
                    description = value
            if len(description) > 23:
                description = description[:23]
            amount = str(format(float(amount), ".2f"))
            if len(amount) > 7:
                amount = amount[:7]
            result += description + str(amount).rjust(30 - len(description)) + "\n"
        result += "Total: " + str(format(float(self.amount), ".2f"))
        return result


def create_spend_chart(categories):
    output = "Percentage spent by category"
    x = len(categories)
    percentages = []
    total_spent = sum(cat.get_withdrawals() for cat in categories)

    for cat in categories:
        raw = cat.get_withdrawals() / total_spent
        percentages.append(int((raw // 0.1) * 10))

    for y in range(100, -1, -10):
        output += "\n"
        output += (
            str(y) + "| "
            if y == 100
            else " " + str(y) + "| "
            if y < 100 and y > 0
            else "  0| "
        )

        for col in range(x):
            output += "o  " if percentages[col] >= y else " " * 3

    output += "\n" + " " * 4 + "-" + "-" * x * 3
    max_name_length = 0

    for cat in categories:
        if len(cat.category) > max_name_length:
            max_name_length = len(cat.category)

    for z in range(max_name_length):
        output += "\n" + " " * 5
        for cat in categories:
            try:
                output += cat.category[z] + " " * 2
            except:
                output += " " * 3

    return output

