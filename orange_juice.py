class Unit:

    def __init__(self, name):
        self.name = name
        self.person = name
        if name == 'You':
            self.person += 'r'
        while True:
            try:
                print(self.person, 'status (HP, ATK, DEF, EVD): ', end='')
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


    def def_result(ATK, defender, action):
        '''return tuple(die_count, total_damage), total_damage counts only if the defender lives'''

        die_count, total_damage = 0, 0
        for roll in range(1, 7):

            if action == 'DEF':
            # try to defend
                damage = max( 1 , ATK - max( 1, defender.DEF + roll) )
            elif action == 'EVD':
            # try to evade
                damage = 0 if defender.EVD + roll > ATK else ATK
                
            if defender.HP > damage:
                total_damage += damage
            else:
                die_count += 1
            
        return die_count, total_damage


    def defensive(ATK, defender):

        for action in 'DEF', 'EVD':

            die_count, total_damage = def_result(ATK, defender, action)

            if die_count == 6:
                print(f'[{action}] CERTAIN DEATH.')
            elif die_count == 0:
                print(f'[{action}] SURVIVE. Avarage damage: {total_damage / 6 :.2f}')
            else:
                print(f'[{action}] {die_count / 6 * 100:.2f}% Die;\n'
                      f'      {(6-die_count) / 6 * 100:.2f}% Survive, avarage damage: {total_damage / (6-die_count):.2f}')



    def offensive(attacker, defender, p = 1):
    # p for possibility

        if p == 0: return

        die_count, total_damage = 0, 0
        for roll in range(1, 7):

            ATK = roll + attacker.ATK
            def_die, def_dmg = def_result(ATK, defender, 'DEF')
            evd_die, evd_dmg = def_result(ATK, defender, 'EVD')

            caution_ratio = 0.8
            # TODO what is the exact caution_bias?

            if def_die * defender.HP + def_dmg > evd_die * defender.HP + evd_dmg + caution_ratio:
            # suppose everyone is 'cautious', viz perfers to defend would they die less
                die_count += evd_die / 6
                total_damage += evd_dmg / 6
            else:
                die_count += def_die / 6
                total_damage += def_dmg / 6

        print(f'[{attacker.name} => {defender.name}]', '(whether happens or not)' if p < 1 else '')
        if die_count == 6:
            print('    CERTAIN DEATH.')
            enemy.HP = 0
        elif die_count == 0:
            print(f'    SURVIVE. Avarage damage: {total_damage * p / (6-die_count):.2f}')
            enemy.HP -= total_damage / (6-die_count)
        else:
            print(f'    {die_count * p / 6 * 100:.2f}% Slain.\n'
                  f'    Avarage damage: {total_damage * p / (6-die_count):.2f}')
            enemy.HP -= enemy.HP * die_count / 6 + total_damage * p / (6-die_count)



    while True:

        print('\nChoose mode (Offend(O/0) or Defend(D/1)): ', end='')
        mode = input().lower()

        if mode in ('d', '1', 'defend', 'def'):
        # User is the defender
            defensive(
                checked_input('Enemy attack: ', int),
                Unit('You')
            )


        elif mode in ('o', '0', 'offend', 'off'):
        # User is the offender
            you = Unit('You')        
            enemy = Unit('Enemy')
            origin_enemy_HP = enemy.HP

            offensive(you, enemy)
            offensive(enemy, you, p = enemy.HP / origin_enemy_HP)

        else:
            print('Nigh!')


if __name__ == "__main__":
    try:
        print('\nYou can press [Ctrl + C] at any time to halt.')
        main()
    except KeyboardInterrupt:
        pass