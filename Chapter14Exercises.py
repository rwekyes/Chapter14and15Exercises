# 14.11.1 Ask A Virtual Assistant

# Claude Opus 5.5 had this to say:
#
# (Delivered in the voice of one Bond, Jamesh Bond. Shaken, not shtirred.)
#
# ---------------------------------------------------------------------------
# Q1: “What ish the difference between a classh and a type?”
# ---------------------------------------------------------------------------
# Ah, Mish Moneypenny, you alwaysh did ashk the beshht queshtionsh.
#
# In modern Python, they're the shame thing, really. A classh *ish* a type.
# When you write `class Time:`, you've jusht created a brand new type,
# shimple ash that. Call `type(lunch)` and Python tellsh you <class 'Time'>.
#
# Historically, "type" meant the built-in onesh, int, shtr, float, and
# "classh" meant the onesh that you and I write ourshelvesh. Python 2.2
# shettled that bit of businessh and unified the two. Now even the
# built-insh are clashesh, and every classh ish itshelf an inshtansh of
# `type`. A tidy arrangement. Very... profeshional.
#
# ---------------------------------------------------------------------------
# Q2: “What ish the difference between an object and an inshtansh?”
# ---------------------------------------------------------------------------
# Shame agent, different cover shtory.
#
# In Python, everything ish an object. Every value, every number, every
# function, even the clashesh themshelvesh. "Inshtansh" ish jusht the word
# we ushe when we want to shay which classh the object belongsh to. `lunch`
# ish an object, yesh, but shpecifically, it ish an *inshtansh of Time*.
#
# Think of it thish way: I'm a man. But I am an inshtansh of the Double-O
# shection. One word ish general, the other tellsh you who I work for.
#
# ---------------------------------------------------------------------------
# Q3: “What ish the difference between a variable and an attribute?”
# ---------------------------------------------------------------------------
# A variable ish a name that livesh out in the open, in a function or at
# the top of your module, and it refersh to an object:
#
#     start = make_time(9, 40, 0)      # `start` ish a variable
#
# An attribute ish a name that belongsh to an object. You reach it with
# the dot, like shliding your hand into a man'sh breasht pocket:
#
#     start.hour                       # `hour` ish an attribute of `start`
#
# Variablesh live in a namespashe (local or global). Attributesh live
# *inshide the object*, and they travel wherever that object goesh. Pash
# `start` to a function, and `hour` comesh along for the ride. Like a
# Walther PPK in a shoulder holshter.
#
# ---------------------------------------------------------------------------
# Q4: “What are the prosh and consh of pure functionsh compared to impure
#      functionsh?”
# ---------------------------------------------------------------------------
# A pure function ish a clean operator. It doeshn't modify itsh argumentsh,
# doeshn't print, doeshn't fiddle with global shtate. It takesh valuesh in
# and handsh a new value back. Like `add_time`, which returnsh a fresh Time
# and leavesh the original untouched. No fingerprintsh.
#
# An impure function, a "modifier", like `increment_time`, changesh the
# object you hand it. Effective, but it leavesh a messh behind.
#
# The prosh of going pure:
#   - Eashier to reashon about. Shame input, shame output, every time.
#   - Eashier to tesht. No hidden shide effectsh to shneak up on you.
#   - Shafer with aliashing. If two variablesh refer to the shame object,
#     a pure function won't shurprishe one of them behind itsh back.
#   - Eashier to reushe and combine, like building blocksh.
#
# The consh:
#   - Shometimesh lesh efficient. Making copiesh coshtsh time and memory,
#     and for large objectsh, modifying in plashe can be fashter.
#   - Shome jobsh *require* shide effectsh. Printing, writing filesh,
#     talking to the network. You can't print a shtring purely, I'm afraid.
#   - Modifiersh can be more convenient when changing the object ish the
#     whole point of the mishion.
#
# Ash the book shaysh: write pure functionsh whenever it'sh reashonable,
# and ushe modifiersh only when there'sh a compelling advantage. A good
# agent only firesh when he hash to.
#
# ---------------------------------------------------------------------------
# Q5: “What format shpeshifiersh can be ushed in a Python f-shtring?”
# ---------------------------------------------------------------------------
# Ah, now we get to the gadgetsh. Q would be proud.
#
# Everything after the colon in `{value:shpec}` followsh thish pattern:
#
#     [[fill]align][sign][z][#][0][width][grouping][.precishion][type]
#
# Alignment and fill:
#   <   left-align          f'{"Bond":<8}'    -> 'Bond    '
#   >   right-align         f'{"Bond":>8}'    -> '    Bond'
#   ^   center              f'{"Bond":*^8}'   -> '**Bond**'
#   =   pad after the sign  f'{-7:=5}'        -> '-   7'
#
# Sign:
#   +   alwaysh show a sign         f'{7:+}'   -> '+7'
#   -   only for negativesh (default)
#   ' ' a shpashe for poshitive numbersh
#
# Width, zero-padding, grouping:
#   f'{7:03d}'          -> '007'       (Naturally.)
#   f'{1000000:,}'      -> '1,000,000'
#   f'{1000000:_}'      -> '1_000_000'
#
# Precishion:
#   f'{3.14159:.2f}'    -> '3.14'
#   f'{"Goldfinger":.4}' -> 'Gold'    (truncatesh a shtring)
#
# Type codesh:
#   Integersh:  d (decimal), b (binary), o (octal), x / X (hex), c (char),
#               n (locale-aware number)
#   Floatsh:    f / F (fixed point), e / E (shientific), g / G (general),
#               % (percentage: f'{0.07:.0%}' -> '7%')
#   Shtringsh:  s
#   The # flag addsh a prefix: f'{255:#x}' -> '0xff', f'{5:#b}' -> '0b101'
#
# Conversionsh (before the colon):
#   !r  ushe repr()    f'{"Bond"!r}'  -> "'Bond'"
#   !s  ushe shtr()
#   !a  ushe ashcii()
#
# And the debugging trick, my pershonal favourite:
#   name = 'Bond'
#   f'{name=}'          -> "name='Bond'"
#
# You've already sheen one in thish chapter, in print_time:
#   f'{time.hour:02d}'  -> zero-padded, two digitsh wide, decimal integer.
#
# That'll be all, Q. ...I'll try to bring the f-shtringsh back in one piesh.

class Time:
    """Represents a time of day."""

def print_time(time):
    s = f'{time.hour:02d}:{time.minute:02d}:{time.second:02d}'
    print(s)

def make_time(hour, minute, second):
    time = Time()
    time.hour = hour
    time.minute = minute
    time.second = second
    return time

def increment_time(time, hours, minutes, seconds):
    time.hour += hours
    time.minute += minutes
    time.second += seconds

    carry, time.second = divmod(time.second, 60)
    carry, time.minute = divmod(time.minute + carry, 60)
    carry, time.hour = divmod(time.hour + carry, 24)

def time_to_int(time):
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds

def int_to_time(seconds):
    minute, second = divmod(seconds, 60)
    hour, minute = divmod(minute, 60)
    return make_time(hour, minute, second)

def add_time(time, hours, minutes, seconds):
    duration = make_time(hours, minutes, seconds)
    seconds = time_to_int(time) + time_to_int(duration)
    return int_to_time(seconds)


# 14.11.2 Exercise:

def subtract_time(t1, t2):
    t1_sec = time_to_int(t1)
    t2_sec = time_to_int(t2)
    if t1_sec > t2_sec:
        return int_to_time(t1_sec - t2_sec)
    else:
        return int_to_time(t2_sec - t1_sec)

# 14.11.3 Exercise:

def is_after(t1, t2):
    """Checks whether `t1` is after `t2`.

    >>> is_after(make_time(3, 2, 1), make_time(3, 2, 0))
    True
    >>> is_after(make_time(3, 2, 1), make_time(3, 2, 1))
    False
    >>> is_after(make_time(11, 12, 0), make_time(9, 40, 0))
    True
    """
    if time_to_int(t1) > time_to_int(t2):
        return True
    return False

# 14.11.4 Exercise

class Date:
    """Represents a year, month, and day"""

def make_date(year, month, day):
    date = Date()
    date.year = year
    date.month = month
    date.day = day
    return date

def print_date(date):
    print(f"{date.year}-{date.month}-{date.day}")

def is_after(date1, date2):
    if date1.year > date2.year:
        return True
    if date1.year == date2.year:
        if date1.month > date2.month:
            return True
        elif date1.month == date2.month:
            if date1.day > date2.day:
                return True
    return False

date1 = make_date(1933, 6, 22)
date2 = make_date(1933, 9, 17)

print_date(date1)
print_date(date2)
print(is_after(date1, date2))