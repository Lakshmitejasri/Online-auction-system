class User:
    def __init__(self, name):
        self.name = name

class Bid:
    def __init__(self, user, amount):
        self.user = user
        self.amount = amount

class Auction:
    def __init__(self, item, starting_price):
        self.item = item
        self.starting_price = starting_price
        self.bids = []
        self.highest_bidder = None

    def place_bid(self, user, amount):
        if amount > self.starting_price and (not self.bids or amount > self.get_highest_bid().amount):
            self.bids.append(Bid(user, amount))
            self.highest_bidder = user
            self.starting_price = amount  # Update the starting price to the new highest bid
            print(f"Bid placed by {user.name} for ${amount}")
        else:
            print("Bid not accepted. Must be higher than current bid.")

    def get_highest_bid(self):
        return self.bids[-1] if self.bids else None

    def display_auction_details(self):
        print(f"Auction for: {self.item}")
        print(f"Starting Price: ${self.starting_price}")
        highest_bid = self.get_highest_bid()
        if highest_bid:
            print(f"Highest Bid: ${highest_bid.amount} by {highest_bid.user.name}")
        else:
            print("No bids yet.")

def main():
    auction = Auction("Antique Vase", 100.0)

    auction.display_auction_details()

    while True:
        user_name = input("Enter your name (or 'exit' to quit): ")
        if user_name.lower() == 'exit':
            break

        user = User(user_name)

        bid_amount = float(input("Enter your bid amount: "))
        auction.place_bid(user, bid_amount)
        auction.display_auction_details()

if __name__ == "__main__":
    main()
