class Solution:

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        from collections import defaultdict

        if endWord not in wordList: return 0
        queue = [(beginWord, 1)]
        combo_dict = defaultdict(list)

        for word in wordList:
            for i in range(len(word)):
                combo_dict[word[:i] + "*" + word[i + 1:]].append(word)

        # wordList.append(endWord)
        visited = set([beginWord])  # at this step, visited nodes
        # print(combo_dict)

        while (queue):
            tmp, step = queue.pop(0)
            for i in range(len(word)):
                intermediate_word = tmp[:i] + "*" + tmp[i + 1:]
                # print("candidates:", combo_dict[intermediate_word])
                for word in combo_dict[intermediate_word]:
                    if word == endWord:
                        return step + 1
                    if word not in visited:
                        # print("tmp:", tmp, "word:", word, visited)

                        queue.append((word, step + 1))
                        visited.add(word)

            # print(queue)

            # print("word=", word, queue, visited)
        return 0
