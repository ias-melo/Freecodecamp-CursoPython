class Category:

    def __init__(self, name):

        self.name = name

        self.ledger = []

    def deposit(self, amount, description=""):

        self.ledger.append({

            "amount": amount,

            "description": description

        })

    def withdraw(self, amount, description=""):

        if self.check_funds(amount):

            self.ledger.append({

                "amount": -amount,

                "description": description

            })

            return True

        return False

    def get_balance(self):

        balance = 0

        for item in self.ledger:

            balance += item["amount"]

        return balance

    def check_funds(self, amount):

        return amount <= self.get_balance()

    def transfer(self, amount, category):

        if not self.check_funds(amount):

            return False

        self.withdraw(amount, f"Transfer to {category.name}")

        category.deposit(amount, f"Transfer from {self.name}")

        return True

    def __str__(self):

        result = self.name.center(30, "*") + "\n"

        for item in self.ledger:

            description = item["description"][:23]

            amount = f"{item['amount']:.2f}"

            result += f"{description:<23}{amount:>7}\n"

        result += f"Total: {self.get_balance():.2f}"

        return result

def create_spend_chart(categories):
    
    res = "Percentage spent by category\n"
    
   
    spent = []
    for cat in categories:
        cat_spent = sum(-item["amount"] for item in cat.ledger if item["amount"] < 0)
        spent.append(cat_spent)
    
    total_spent = sum(spent)
   
    percents = [int((s / total_spent) * 100) // 10 * 10 if total_spent > 0 else 0 for s in spent]
    
    
    for i in range(100, -1, -10):
        res += f"{i:>3}| "
        for p in percents:
            res += "o  " if p >= i else "   "
        res += "\n"
        
 
    res += "    " + "-" * (len(categories) * 3 + 1) + "\n"
    
   
    names = [cat.name for cat in categories]
    max_len = max(len(name) for name in names)
    
    for i in range(max_len):
        res += "     "
        for name in names:
            char = name[i] if i < len(name) else " "
            res += f"{char}  "
        if i < max_len - 1:
            res += "\n"
            
    return res
