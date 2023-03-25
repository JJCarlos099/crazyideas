# concatenate character strings
# The program will match a phrase to a phrase given by the user.


def phrase(adjective,verb1,verb2,pluralNoun):
    print(f'Programming is so {adjective} I always get excited because I love {verb1} problems. Learn to {verb2} with '
          f'freecodecamp and reach your {pluralNoun}')


if __name__ == '__main__':
    adjective = input("Adjective: ")
    verb1 = input("Verb: ")
    verb2 = input("Verb: ")
    pluralNoun = input("Plural Noun: ")
    phrase(adjective, verb1, verb2, pluralNoun)
