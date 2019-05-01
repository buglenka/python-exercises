#!/usr/local/bin/Python3.7

"""Replace Words

In English, we have a concept called root, which can be followed 
by some other words to form another longer word - let's call this 
word successor. For example, the root an, followed by other, which 
can form another word another.

Now, given a dictionary consisting of many roots and a sentence. 
You need to replace all the successor in the sentence with the root 
forming it. If a successor has many roots can form it, replace it 
with the root with the shortest length.

You need to output the sentence after the replacement.

Example 1:

Input: dict = ["cat", "bat", "rat"]
sentence = "the cattle was rattled by the battery"
Output: "the cat was rat by the bat"
 

Note:

The input will only have lower-case letters.
1 <= dict words number <= 1000
1 <= sentence words number <= 1000
1 <= root length <= 100
1 <= sentence words length <= 1000
"""

from typing import List

def replaceWords(dict: List[str], sentence: str) -> str:
    initial_words = sentence.split()
    words = set(initial_words)

    # Make optimization for speed up search in dict
    dict.sort(key=lambda x: len(x))
    len_dict = {}

    for w in dict:
        l = len(w)
        if l in len_dict:
            len_dict[l].append(w)
        else:
            len_dict[l] = [w]

    replacements = {}

    for word in words:
        # Find all possible roots
        i = 0
        while(i < len(word)-1):
            root = ''
            found = False

            for j in range(i, len(word)-1):
                root += word[j]
                l = len(root)

                if (l in len_dict) and (root in len_dict[l]):
                    found = True

                    if (word in replacements): 
                        if (len(root) < len(replacements[word])):
                            replacements[word] = root
                    else:
                        replacements[word] = root

                    break
            
            if found:
                i += len(root)
            else:
                break
            
    for i in range(len(initial_words)):
        w = initial_words[i]

        if (w in replacements):
            initial_words[i] = replacements[w]

    return " ".join(initial_words)

sentence = "the cattle was rattled by the battery"
dict = ["cat", "bat", "rat"]


print(replaceWords(dict, sentence))


