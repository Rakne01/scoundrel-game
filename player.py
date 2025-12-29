
from constants import SCOUNDREL_STARTING_HEALTH

########################PLAYER FUNCTIONS##################################
class Player:
    def __init__(self, health):
        self.health = health
        self.weapon = None  # Weapon slot starts empty
        self.last_monster_slain = None #Track last kill for weapon.
    
    def is_alive(self):
        return self.health > 0

    def equip_weapon(self, card):
        if card.suit != "Diamonds":
            print("This card is not a weapon!")
            return False
        
        if self.weapon is None:
            # No weapon equipped, just equip it
            print(f"Equipping {card}")
            self.weapon = card
            return True
        
        # Already have a weapon, give player a choice
        print(f"\nCurrent weapon: {self.weapon} (Rank: {self.weapon.rank})")
        print(f"New weapon: {card} (Rank: {card.rank})")
        if self.last_monster_slain:
            print(f"Last monster slain: {self.last_monster_slain} (Rank: {self.last_monster_slain.rank})")
                
        while True:
            choice = input("Replace your weapon? (yes/no): ").lower()
            if choice in ['yes', 'y']:
                print(f"Discarding {self.weapon} to equip {card}")
                self.weapon = card
                self.last_monster_slain = None  # Reset progression when changing weapons
                return True
            elif choice in ['no', 'n']:
                print(f"Keeping {self.weapon}, discarding {card}")
                return False
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")
    
    def heal(self, card):
        if card.suit != "Hearts":
            print("This card is not a potion!")
            return False
        
        heal_amount = card.rank_index + 2
        max_heal = min(heal_amount,SCOUNDREL_STARTING_HEALTH - self.health)
        self.health += max_heal
        
        print(f"Healed for {max_heal} HP!")
        return True

    def take_damage(self, card):
        if card.suit != "Spades" and card.suit != "Clubs":
            print("This card is not a monster!")
            return False
        
        monster_damage = card.rank_index + 2
            
        ###takes full damage if no weapon equipped
        if self.weapon is None:
            # No weapon, take full damage
            print(f"No weapon! Taking {monster_damage} damage!")
            self.health -= monster_damage
        else:
            weapon_damage = self.weapon.rank_index + 2
            # Check if weapon can be used (monster must be weaker than last kill)
            if self.last_monster_slain is not None and card.rank_index >= self.last_monster_slain.rank_index:
                # Monster is too strong compared to last kill
                print(f"Monster too strong for your weapon! Taking {monster_damage} damage!")
                self.health -= monster_damage
            elif weapon_damage >= monster_damage:
                # Weapon kills the monster
                damage_taken = 0
                print(f"Monster slain with your weapon!")
                self.last_monster_slain = card  # Track this kill
            else:
                # Weapon reduces damage but doesn't kill
                damage_taken = monster_damage - weapon_damage
                print(f"Weapon reduces damage! Taking {damage_taken} damage!")
                self.health -= damage_taken
                self.last_monster_slain = card  # Track this kill

        if self.health <= 0:
            print("Game Over")


    def display_status(self):
        print(f"\nHealth: {self.health}")
        if self.weapon:
            weapon_info = f"Weapon: {self.weapon}"
            if self.last_monster_slain:
                weapon_info += f" (Last kill: {self.last_monster_slain})"
            print(weapon_info)
        else:
            print("Weapon: None")