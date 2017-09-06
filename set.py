bri = set(['brazil', 'russia', 'india'])
bri2 = {'brazil', 'russia', 'india'}

print('brazil' in bri)
print('usa' in bri)

bric = bri.copy()
bric.add('china')

print(bric.issuperset(bri))

bri.remove('russia')

# 토나오게 사기다. 이게 말이 되는 건가??
print(bri & bric)

