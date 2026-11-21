# 15.10.1 Ask a Virtual Assistant

# Claude Opus 5.5 had this to say:
#
# (Transcribed from the crypt of Count Vladislav, Lord of the Night,
#  four hundred years undead, and as of Tuesday, Hepatitis C positive.)
#
# ---------------------------------------------------------------------------
# Q1: “What's the difference between an instance method and a static method?”
# ---------------------------------------------------------------------------
# Forgive me, mortal. I have just returned from the clinic. Four centuries
# I have stalked the night. I have fed upon dukes. Upon bishops. Upon a
# rather tannic Hapsburg. And it was not the plague, nor the stake, nor the
# dawn that finally laid me low. It was one impulsive bite outside a
# comedy club in Van Nuys. Andy Dick. I bit Andy Dick. The doctor did not
# even look surprised.
#
# But you ask about methods. Very well. It distracts me from my liver.
#
# An INSTANCE METHOD is defined inside a class and takes `self` as its
# first parameter. You call it ON an instance, and that instance is
# passed in automatically as `self`. It can read and change the
# instance's attributes. It knows exactly whose neck it is attached to:
#
#     class Time:
#         def time_to_int(self):
#             minutes = self.hour * 60 + self.minute
#             return minutes * 60 + self.second
#
#     start.time_to_int()    # `start` becomes `self`
#
# A STATIC METHOD is marked with the @staticmethod decorator and takes
# no `self` at all. It lives in the class's namespace, but it is not
# bound to any instance. It cannot touch instance attributes, because it
# has no instance. You usually call it on the class itself:
#
#     class Time:
#         @staticmethod
#         def int_to_time(seconds):
#             minute, second = divmod(seconds, 60)
#             hour, minute = divmod(minute, 60)
#             return make_time(hour, minute, second)
#
#     Time.int_to_time(3661)
#
# The book makes int_to_time static for a good reason: its whole job is
# to CREATE a Time object, so there is no Time yet to call it on. A
# static method is for work that belongs with the class but does not
# need any particular victim.
#
# An instance method, you see, always knows exactly who it is feeding
# on. A static method takes its arguments and asks no questions. I, too,
# once asked no questions. Look where it got me.
#
# ---------------------------------------------------------------------------
# Q2: “Why are static methods called static?”
# ---------------------------------------------------------------------------
# *coughs into a velvet handkerchief* Ah. Mostly history, I am afraid,
# like most things about me.
#
# The word comes from C++ and Java, where the `static` keyword marks
# members that belong to the class itself rather than to each object.
# Those languages inherited "static" from C, where it meant storage that
# is set up once and stays put for the life of the program instead of
# being created fresh on each call.
#
# In Python the name still fits one way: a static method never changes
# depending on which instance you reach it through. A normal method gets
# "bound" to its object at the moment you access it (`start.time_to_int`
# remembers `start`). A static method is never bound. Whether you call
# Time.int_to_time or start.int_to_time, you get the very same plain
# function. It stays fixed. Static. Unmoved.
#
# Rather like my viral load, the hepatologist tells me.
#
# ---------------------------------------------------------------------------
# Q3: “Rewrite this function as a method of the Time class.”
#
#     def subtract_time(t1, t2):
#         return time_to_int(t1) - time_to_int(t2)
# ---------------------------------------------------------------------------
# The first parameter becomes `self`. The second I shall call `other`,
# which is the convention when a method takes another object of the same
# class. And since time_to_int is itself a method in Chapter 15, we call
# it with dot notation on each one:
#
#     class Time:
#         """Represents a time of day."""
#
#         def time_to_int(self):
#             minutes = self.hour * 60 + self.minute
#             seconds = minutes * 60 + self.second
#             return seconds
#
#         def subtract_time(self, other):
#             return self.time_to_int() - other.time_to_int()
#
# Usage:
#
#     start = make_time(9, 40, 0)
#     end = make_time(11, 12, 0)
#     end.subtract_time(start)     # -> 5520 seconds
#
# Note the order: `end.subtract_time(start)` means end minus start, just
# as subtract_time(end, start) did before. The object before the dot
# takes the place of the first argument.
#
# And if you wish to be truly elegant, you may name it __sub__ instead,
# and Python will let you write `end - start`. Operator overloading. Very
# refined. Very aristocratic.
#
# 5520 seconds. Ninety-two minutes. That is about how long I stood in the
# alley afterward, staring at the moon, wondering why I did not simply
# bite the bouncer.
#
# Learn from me, child of the day. Validate your inputs. Check what you
# are sinking your teeth into before you commit. And for the love of all
# that is unholy, stay out of Van Nuys.

# 15.10.2

class Date:

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __str__(self):
        return str(self.year) + "-" + str(self.month) + "-" + str(self.day)

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

date1 = Date(1933, 6, 22)
date2 = Date(1933, 9, 17)

print(date1)
print(date2)
print(is_after(date1, date2))