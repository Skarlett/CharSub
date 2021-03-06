# CharSub
Uses rulesets to substitute characters in a seperate squence of characters. Create about 99% of possibilties.

Example Output: https://pastebin.com/6CgXcUGn

## Basic usage
     from charsub import Substitute
     
     a = Substitute({'.':'A'})
     print(a.deform('...'))
     >>> ['...', 'A..', '.A.', '..A', 'AA.', 'A.A', '.AA', 'AAA']
--------
## Advanced
    from charsub import Substitute
    import charsub.patterns as patterns
    
    print(Substitute().deform('password', entrophy_level=5, entrophy_start=1, deformFuncList=[patterns.modulus]))

## Debug
--------
    import charsub.debugTools as debugtools
    from charsub import Substitute
    
    debugtools.patternComparsion(Substitute(), 'password', verbose=True)
    
 ### Speed
-------
    $ time python -c "from charsub import Substitute; len(Substitute().deform('password'))"

     real    0m1.865s
     user    0m1.848s
     sys     0m0.004s

### Cpu info
------
    $ lscpu
    Architecture:          x86_64
    CPU op-mode(s):        32-bit, 64-bit
    Byte Order:            Little Endian
    CPU(s):                4
    On-line CPU(s) list:   0-3
    Thread(s) per core:    2
    Core(s) per socket:    2
    Socket(s):             1
    NUMA node(s):          1
    Vendor ID:             GenuineIntel
    CPU family:            6
    Model:                 58
    Model name:            Intel(R) Core(TM) i5-3320M CPU @ 2.60GHz
    Stepping:              9
    CPU MHz:               1241.601
    CPU max MHz:           3300.0000
    CPU min MHz:           1200.0000
    BogoMIPS:              5188.45
    Virtualization:        VT-x
    L1d cache:             32K
    L1i cache:             32K
    L2 cache:              256K
    L3 cache:              3072K
    NUMA node0 CPU(s):     0-3
    Flags:                 fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx rdtscp lm constant_tsc arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc aperfmperf eagerfpu pni pclmulqdq dtes64 monitor ds_cpl vmx smx est tm2 ssse3 cx16 xtpr pdcm pcid sse4_1 sse4_2 x2apic popcnt tsc_deadline_timer aes xsave avx f16c rdrand lahf_lm epb tpr_shadow vnmi flexpriority ept vpid fsgsbase smep erms xsaveopt dtherm ida arat pln pts
### Bare requirements
  + 512KB RAM (2Gb recommended for larger data sets)
  + CPU - I dunno
  
