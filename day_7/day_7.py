class Hand:
  strengths = list("AKQT") + [str(i) for i in range(9, 1, -1)] + ["J"]

  def __init__(self, hand: str, bid: int):
    self.hand = hand
    self.bid = bid

    self.cards, self.counts = self.get_cards_counts(self.hand)

  def get_cards_counts(self, hand):
    cards_counts = {i: hand.count(i) for i in set(hand) if i != "J"}
    cards = sorted(cards_counts, key=lambda x: cards_counts[x], reverse=True)
    counts = [cards_counts[i] for i in cards]

    if not counts:
      # Use max.
      cards = ["A"]
      counts = [5]
    else:
      counts[0] += hand.count("J")

    return (cards, counts)

  def __lt__(self, other) -> bool:
    for (c, oc) in zip(self.counts, other.counts):
      if c == oc:
        continue
      return c < oc

    for (c, oc) in zip(self.hand, other.hand):
      if c == oc:
        continue
      return Hand.strengths.index(c) > Hand.strengths.index(oc)
  
  def __repr__(self) -> str:
    return f"Hand(hand=\"{self.hand}\", bid={self.bid}))"


with open("data.txt") as f:
  data = f.read().split()

hands = [Hand(h, int(b)) for (h, b) in zip(data[::2], data[1::2])]
hands = sorted(hands)

winnings = 0
for (i, hand) in enumerate(hands):
  winnings += (i + 1) * hand.bid

print(winnings)
