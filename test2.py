'''
Created on 2014/01/31

@author: Tukasa
'''
def askok(prompt, retries = 4, complaint = 'Yes or no, please !'):
    while True:
        ok = input(prompt)

        if ok in('y', 'ye', 'yes'):
            return True
        if ok in('n', 'no', 'nop', 'nope'):
            return False

        retries = retries - 1

        if retries < 0:
            raise IOError('refusenik user')

        print(complaint)
        
fire = askok('Hi.')

print(fire)
