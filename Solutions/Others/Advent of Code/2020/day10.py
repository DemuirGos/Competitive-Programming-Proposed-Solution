strin=list(set(map(int,open("InputData\day10.txt", "r").read().split('\n'))))
def part1diff(s):
    return len([i for i in list(zip(s,s[1:])) if i[1] - i[0] == 1])*len([i for i in list(zip(s,s[1:])) if i[1] - i[0] == 3])
def part2path(v,d,stp,update):
    return max([update(v,d,adapter,step) for adapter in d for step in stp if adapter + step in d])
part1=part1diff([0]+strin.copy()+[max(strin)+3])
part2=part2path(max(strin)+3,dict(map(lambda x:(x,x==0 and 1 or 0),[0]+strin.copy()+[max(strin)+3])),[1,2,3],lambda v,d,adapter,step:d.update({adapter+step:d[adapter+step]+d[adapter]}) or d[v])
