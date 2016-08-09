adrian = dict()
adrian['name'] = 'Adrian'
adrian['sequence'] = 'ABC'
adrian['p'] = 0 
adrian['len'] = len(adrian['sequence'])

bruno = dict()
bruno['name'] = 'Bruno'
bruno['sequence'] = 'BABC'
bruno['p'] = 0 
bruno['len'] = len(bruno['sequence'])

goran = dict()
goran['name'] = 'Goran'
goran['sequence'] = 'CCAABB'
goran['p'] = 0 
goran['len'] = len(goran['sequence'])

participants = [adrian, bruno, goran]

input() # dont need this one
s = input()

for i, l in enumerate(s):
    for p in participants:
        p['p'] += l == p['sequence'][i % p['len']]

participants = sorted(participants, key = lambda p: (-p['p'], p['name']))

highest_p = participants[0]['p']
print(highest_p)
for p in participants:
    if p['p'] == highest_p:
        print(p['name'])
    else:
        break

