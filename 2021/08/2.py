#!python.exe
import argparse
import sys
parser = argparse.ArgumentParser()
parser.add_argument(
    '-t', '--test', help="Run with test input", action='store_true')
args = parser.parse_args()


def getInput(file="input"):
    path=sys.path[0]
    if args.test:
        file = "test_input"
    with open(f"{path}/{file}", "r") as f:
        lines = f.read()
        return lines.splitlines()

def parse(input):
    dprint(input)
    inputs=input.split(' | ')[0]
    outputs=input.split(' | ')[1]
    # dprint(inputs)
    # dprint(outputs)
    inputs=inputs.split(' ')
    outputs=outputs.split(' ')
    # dprint(inputs)
    # dprint(outputs)
    return(inputs,outputs)

def dprint(msg):
    if args.test:
        print(msg)

def check(known, test):
    for k in known:
        if k not in test:
            return False
    return True

def swap(a,b):
    t=a
    a=b
    b=t
    return a,b

def missing(a,b):
    if len(a)<len(b):
        a,b=swap(a,b)
        
    for i in a:
        if i not in b:
            return i

import itertools
def main():
    sum=0
    
    input = getInput()
    for line in input:
        # line = input[0]
        segs=['']*7
        BCD={}
        ins,outs=parse(line)
        ins = sorted(ins, key=len)
        for i in ins:
            if len(i) == 2: BCD.update({1:i})
            if len(i) == 4: BCD.update({4:i})
            if len(i) == 3: BCD.update({7:i})
            if len(i) == 7: BCD.update({8:i})
        # dprint(BCD)
        #get top seg
        segs[0] = missing(BCD[1], BCD[7])
        for i in ins:
            if len(i) == 5 and check(BCD[1],i): 
                BCD.update({3:i})
                # dprint(BCD)
        # get middle seg
        for i in BCD[3]:
            if i in BCD[4] and i not in BCD[1]:
                segs[6]=i
        # get bottom seg
        for i in BCD[3] :
            if i not in BCD[1] and i not in segs:
                segs[3]=i        
                
        for i in ins:
            if len(i) == 6 and check(BCD[3],i):
                BCD.update({9:i})
        for i in ins:
            if len(i) == 6 and not check(segs[6],i):
                BCD.update({0:i})
        for i in ins:
            if len(i) == 6 and i not in BCD.values():
                BCD.update({6:i})
        for i in BCD[1]:
            if i in BCD[6]: segs[2]=i
            else: segs[1] =i
        for i in BCD[9]:
            if i not in segs:
                segs[5]=i
        for i in range(97,104):
            i=chr(i)
            if i not in segs:
                segs[4]=i
        for i in ins:
            if len(i) == 5 and i not in BCD.values():
                if check(segs[5],i): BCD.update({5:i})
                elif check(segs[4],i): BCD.update({2:i})
        # dprint(list(itertools.permutations(BCD.values())))
        dprint(sorted((key,value) for (key,value) in BCD.items()))
        dprint(segs)
        val=''
        
        for out in outs:
            tests=list(itertools.permutations(out))
            for test in tests:
                test="".join(test)
                for d,b in BCD.items():
                    if test == b:
                        val+=str(d)
        dprint(val)
        sum+=int(val)
    print(sum)

        

        
            
        


main()