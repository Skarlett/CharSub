__title__ = 'charsub'
__version__ = '0.2.5.1'
__author__ = 'Skarlett'
__desc__ = 'This library is a framework designed for string manipulation, bruteforces, extra tools,' \
           'and giving every possiblity for a string input | A password generating toolset'
__doc__ = __desc__


from charsub.sub import Substitute


# I really loved this project because it was logically intensive.

# Since no libraries really supported the things I wanted, and I couldn't find iterchains too useful so...
# Welcome to my word subsitution/permutation part - This was actually my very first of the library.
# This has been rewritten a few times, so you might find bad code or useless functions -
# I plan to write it a few more times, and hopefully thin down the memory use as much as possible

# I would really love to have everything be a generator (keyword: yield), and
# have options to write to disk instead of using memory. Although, I haven't got flush & fsync to work
# This would accomplish a lot of memory tasks with minial memory usage - although slower
# But allowing very weak machines to run this, my machine has 16gb of memory and I see this easily jump to 4gb or 6gb
