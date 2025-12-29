from constants import SCOUNDREL_STARTING_HEALTH
from deck import Deck
from player import Player
from rules import TITLE, RULES


########################GAME FLOW FUNCTIONS##################################
def choose_card(current_room, player):
    while True:
        print("\nCurrent Room:")
        for i, card in enumerate(current_room, 1):
            print(f"{i}. {card}")
        
        choice = get_input("\nChoose a card (1-4): ", player)
        
        # Validate input
        try:
            index = int(choice)
            if 1 <= index <= 4:
                return index - 1  # Convert to 0-based index
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number.")

##to create score calc at the end.
def calculate_score():
    pass

def get_input(prompt, player=None):
    while True:
        user_input = input(prompt)
        
        if user_input.lower() == 'rules':
            print(RULES)
            continue  # Ask again
        
        if user_input.lower() == 'status' and player:
            player.display_status()
            continue  # Ask again
        
        if user_input.lower() == 'exit':
            print("Exiting game...")
            exit()
        
        return user_input  # Return the actual choice


########################MAIN##################################
def main():
    print(f"{TITLE}")
    print("\nWelcome to Scoundrel!")
    
    deck = Deck()
    player = Player(SCOUNDREL_STARTING_HEALTH)
    skips_remaining = 1  # Reset skips for each new room
    
    while player.is_alive() and deck.cards_remaining() >= 4:
        current_room = []
        
        # Draw 4 cards for the room
        for i in range(4):
            card = deck.draw()
            current_room.append(card)
        
        # Room loop - allows skip/play decision after refills
        room_active = True
        while room_active and player.is_alive():
            # Display the room
            print("\nCurrent Room:")
            for i, card in enumerate(current_room, 1):
                print(f"{i}. {card}")
            
            # Get player decision
            if skips_remaining > 0:
                print(f"\nSkips remaining: {skips_remaining}")
                choice = get_input("Enter 'play' to enter the room or 'skip' to skip: ", player).lower()
            else:
                print("\nNo skips remaining!")
                choice = 'play'
            
            if choice == 'skip' and skips_remaining > 0:
                print("Skipping room...")
                deck.return_to_bottom(current_room)
                skips_remaining -= 1
                room_active = False  # Exit room loop to draw new room
                continue
            
            # If they chose to play, proceed with room
            print("Entering room...")
            
            room_heal_used = False
            
            # Player chooses cards until room is cleared or needs refill
            while len(current_room) > 1 and player.is_alive():
                card_index = choose_card(current_room)
                chosen_card = current_room[card_index]
                
                print(f"\nYou chose: {chosen_card}")
                
                # Handle the card based on suit
                if chosen_card.suit == "Diamonds":
                    player.equip_weapon(chosen_card)
                    current_room.pop(card_index)
                
                elif chosen_card.suit == "Hearts":
                    if room_heal_used:
                        print(f"\nHeal already used for this room!")
                    else:
                        player.heal(chosen_card)
                        room_heal_used = True
                    current_room.pop(card_index)
                
                elif chosen_card.suit in ["Spades", "Clubs"]:
                    player.take_damage(chosen_card)
                    current_room.pop(card_index)
                    
                    if not player.is_alive():
                        print("\n=== GAME OVER ===")
                        print(f"You were defeated!")
                        break
                
                player.display_status()
                
                # Check if room needs refilling
                if len(current_room) == 1:
                    print("\n--- Refilling room ---")
                    
                    # Check if we have enough cards to refill
                    if deck.cards_remaining() < 3:
                        print("\n=== VICTORY ===")
                        print("Not enough cards to refill the room. You survived!")
                        return
                    
                    cards_to_draw = 3
                    
                    for _ in range(cards_to_draw):
                        card = deck.draw()
                        current_room.append(card)
                    
                    print(f"Drew {cards_to_draw} new cards!")
                    
                    # Reset skip and break to show room again
                    skips_remaining = 1
                    room_heal_used = False  # Reset heal for new room
                    break  # Break inner loop to show room and ask skip/play
            
            # If we finished the inner loop without refilling, exit room
            if len(current_room) <= 1:
                room_active = False
    
    if player.is_alive():
        print("\n=== VICTORY ===")
        print("You survived all the rooms!")
    

if __name__ == "__main__":
    main()