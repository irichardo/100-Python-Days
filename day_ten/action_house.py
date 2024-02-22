from typing import Optional


class Participant:
    def __init__(self, name: str, bid: int):
        self.name = name
        self.bid = bid


def participant_controller(name: str, bid: int, participants: list):
    participant = Participant(name, bid)
    participants.append(participant)
    
def auction_controller(participants:list[Participant]):
    actual_winner: Optional[Participant] = None
    for participant in participants:
        if actual_winner is None or actual_winner.bid < participant.bid:
            actual_winner = participant
    return actual_winner

def auction_house():
    winner = False
    participants: list[Participant] = []
    while winner == False:
        """
        while winner is not decided the auction continue
        """
        name = input("Introduce your name: ")
        bid = int(input("Introduce your bid, please: "))
        participant_controller(name, bid, participants)
        decision = input("¿You want to continue adding users? type Y/N: \n").upper()
        if decision == "N":
            auction_winner = auction_controller(participants)
            winner = True
            print(f"Congratulations, the winner is {auction_winner.name}")
        elif decision == "Y":
            continue
        else:
            print("Invalid decision, stopping the application")
            break

auction_house()
