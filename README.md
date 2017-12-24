# CharSub
Uses rulesets to substitute characters in a seperate squence of characters. Create about 99% of possibilties.
     
     from charsub import Substitute
     
     a = Substitute({'.':'A'})
     print(a.deform('...'))
     >>> ['A..', '.A.', '..A']
--------
### output from "password"
https://pastebin.com/raw/FQbDnUHH
