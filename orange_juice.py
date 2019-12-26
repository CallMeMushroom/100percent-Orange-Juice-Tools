class Unit:

    def __init__(self, name):
        self.name = name
        while True:
            try:
                print(self.name, 'status (HP, ATK, DEF, EVD): ', end='')
                self.HP, self.ATK, self.DEF, self.EVD = map(int, input().split())
                break
            except:
                pass



def main():
    '''https://github.com/CallMeMushroom/100percent-Orange-Juice-Tools'''

    def checked_input(prompt_str, type_func):
        while True:
            try:
                print(prompt_str, end='')
                return type_func(input())
            except:
                pass


    def defensive(ATK, defender, action):

        die_count, total_damage = 0, 0
        for roll in range(1, 7):

            if action == 'DEF':
            # try to defend
                damage = max( 1 , ATK - (defender.DEF + roll) )
            elif action == 'EVD':
            # try to evade
                damage = 0 if defender.EVD + roll > ATK else ATK
                
            if defender.HP > damage:
                total_damage += damage
            else:
                die_count += 1
            
        return die_count, total_damage

        
    def offensive(attacker, defender):
        
        print('Offensive mode is working in progress.')
        return
        # WORKING IN PROGRESS


    while True:
        print('\nChoose mode (Offensive(O/0) or Defensive(D/1)): ', end='')
        mode = input().lower()

        if mode in ('d', '1', 'defensive', 'def'):
        # User is the defender
            ATK = checked_input('Enemy attack: ', int)
            you = Unit('Your')

            for action in 'DEF', 'EVD':

                die_count, total_damage = defensive(ATK, you, action)
                if die_count == 6:
                    print(f'[{action}] CERTAIN DEATH.')
                else:
                    print(f'[{action}] {die_count / 6 * 100:.2f}% Die;')
                    print(' ' * 5, f'{(6-die_count) / 6 * 100:.2f}% Survive, \
                        avarage damage: {total_damage / (6-die_count):.2f}.')


        elif mode in ('o', '0', 'offensive', 'off'):
        # User is the offender
            you = Unit('Your')        
            enemy = Unit('Enemy')

            offensive(you, enemy)
            if enemy.HP > 0:
                offensive(enemy, you)

        else:
            print('Nigh!')


if __name__ == "__main__":
    try:
        print('\nYou can press [Ctrl + C] at any time to halt.')
        main()
    except KeyboardInterrupt:
        pass