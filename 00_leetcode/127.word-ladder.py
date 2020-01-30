#
# @lc app=leetcode id=127 lang=python
#
# [127] Word Ladder
#

# @lc code=start
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        #method 1.a,单向BFS，用一个queue记录在字典中的单次，访问的深度为queue的层数，和哪一个单次位置并没有关系
        #并且注意由于避免出现环，所以字典中的单次只能使用一次，用一个set来记录访问过的单次
        #之前的做法用一个set来记录访问过的单次和每次更新queue之前删除wordset的元素其实是冗余的，选择其中一种即可
        '''
        if not beginWord or not endWord or not wordList:
            return 0
        if endWord not in wordList:
            return 0
        q = collections.deque([(beginWord, 1)])
        chars = string.ascii_lowercase
        #chars = set("abcdefghijklmnopqrstuvwxyz")
        wordset = set(wordList)
        #visited = set()
        #visited.add(beginWord)
        while q:
            word, depth = q.popleft()
            if word == endWord:
                return depth
            for i in range(len(word)):
                for j in chars:
                    if j != word[i]:
                        new_word = word[:i] + j + word[i+1:]
                        if new_word in wordset:
                            #visited.add(new_word)
                            q.append([new_word, depth+1])
                            wordset.remove(new_word)
        return 0
        '''
        #method 1.b不记录深度，使用一个变量来记录总体深度
        '''
        if not beginWord or not endWord or not wordList or endWord not in wordList:
            return 0
        q = collections.deque([beginWord])
        chars = string.ascii_lowercase
        depth, wordset = 0, set(wordList)
        while q:
            depth +=1
            l = len(q)
            for _ in range(l):
                word = q.popleft()
                if word == endWord:
                    return depth
                for i in range(len(word)):
                    for j in chars:
                        if j != word[i]:
                            newWord = word[:i] + j + word[i+1:]
                            if newWord in wordset:
                                q.append(newWord)
                                wordset.remove(newWord)
        return 0
        '''

        #method 2，双向BFS，使用两个queue分别从头和尾进行BFS，每次队列操作之前判断哪个queue的元素小，从哪一个开始，
        # 优化avarage 时间复杂度
        #这里有个关键点，如果从后端开始搜索，那么搜索的目标已经不是endWord了，目标要变成前一个q中的存在的元素，这样才能交替进行
        #这时候使用queue这种数据结构就不太合适，因为从队列中搜索一个元素效率比较低，我们可以改成set这种
        if not beginWord or not endWord or not wordList or endWord not in wordList:
            return 0
        wordSet = set(wordList)
        s_front, s_end = {beginWord}, {endWord}
        chars, depth = string.ascii_lowercase, 0
        while len(s_front) > 0 and len(s_end) > 0:
            depth +=1
            if len(s_front) > len(s_end):
               s_front, s_end = s_end, s_front
            s_tmp = set()
            for w in s_front:
                for i in range(len(w)):
                    for j in chars:
                        if j != w[i]:
                            newWord = w[:i]+j+w[i+1:]
                            if newWord in s_end:
                                return depth+1
                            if newWord in wordSet:
                                wordSet.remove(newWord)
                                s_tmp.add(newWord)
            s_front = s_tmp
        return 0

            
       
        
# @lc code=end

