# CharSub
Uses rulesets to substitute characters in a seperate squence of characters. Create about 99% of possibilties.
     
     from charsub import Substitute
     
     a = Substitute({'.':'A'})
     print(a.deform('...'))
     >>> ['...', 'A..', '.A.', '..A', 'AA.', 'A.A', '.AA', 'AAA']
--------
    time python -c "from charsub import Substitute;print(len(Substitute().deform('password')))"
    4800
    
    real    0m2.117s
    user    0m2.080s
    sys     0m0.008s

Another output examples https://pastebin.com/6CgXcUGn
