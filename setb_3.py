vowel = "aeiouAEIOU"
def presentperf (verb):
    if verb.endswith("ee") or len(verb) < 3:
        return verb + "ing"
    if verb.endswith("ie"):
        return verb[:-2] + "ying"
    if verb.endswith("e"):
        return verb[:-1] + "ing"
    if verb[-2] in vowel and (verb[-1] not in vowel) and (verb[-3] not in vowel):
        return verb + verb[-1] + "ing"
    else:
        return verb + "ing"


print(presentperf("append"))

