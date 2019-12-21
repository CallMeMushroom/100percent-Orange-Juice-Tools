class Unit():

    def __init__(self):
        self.HP, self.ATK, self.DEF, self.EVD = map(int, input().split())


def main():

    def defensive():

        print('Enemy Attack: ', end='')
        ATK = int(input())

        print('Your status (HP, ATK, DEF, EVD): ', end ='')
        you = Unit()
        

        for action in 'DEF', 'EVD':

            die_count, total_damage = 0, 0
            for roll in range(1, 7):

                if action == 'DEF':
                # try to defend
                    damage = max( 1 , ATK - (you.DEF + roll) )
                elif action == 'EVD':
                # try to evade
                    damage = 0 if you.EVD + roll > ATK else ATK
                
                if you.HP > damage:
                    total_damage += damage
                else:
                    die_count += 1
            
            if die_count == 6:
                print(f'[{action}] CERTAIN DEATH.')
            else:
                print(f'[{action}] {die_count / 6 * 100:.2f}% Die;\n      {(6-die_count) / 6 * 100:.2f}% Survive, avarage damage: {total_damage / (6-die_count):.2f}.')


    def offensive():

        print('Your status (HP, ATK, DEF, EVD): ', end ='')
        you = Unit()
            
        print('Enemy status (HP,ATK, DEF, EVD):')
        enemy = Unit()


    while True:
        print('\nChoose mode (Offensive(O/0) or Defensive(D/1)): ', end='')
        mode = input().lower()
        if mode in ('d', '1', 'defensive', 'def'):
            defensive()
        elif mode in ('o', '0', 'offensive', 'off'):
            offensive()
        else:
            print('Nigh!')


if __name__ == "__main__":
    try:
        print('\nYou can press [Ctrl + C] at any time to halt.')
        main()
    except KeyboardInterrupt:
        pass