from collections import defaultdict, deque

def find_anagrams(words):
    def char_count(word):
        cnt = [0]*26
        for char in word:
            cnt[ord(char)-ord('a')] += 1
        return tuple(cnt)

    anagrams = defaultdict(list)

    for word in words:
        key = char_count(word)
        anagrams[key].append(word)

    filterd = [group for group in anagrams.values() if len(group) > 1]
    return [word for group in filterd for word in group]

def to_sorted_linked_list(words):
    sorted_words = sorted(words)
    return deque(sorted_words)

###### ANSWER ######
def anagrams_to_sorted_linked_list(words):
    anagrams = find_anagrams(words)
    return to_sorted_linked_list(anagrams)

words = ["pool", "loco", "cool", "stain", "satin", "pretty", "nice", "dne", "goog", "traart", "end", "loop"]
result = anagrams_to_sorted_linked_list(words)
print(" -> ".join(result))