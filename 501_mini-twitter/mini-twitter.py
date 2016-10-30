# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/mini-twitter
@Language: Python
@Datetime: 16-06-24 11:35
'''

'''
Definition of Tweet:
class Tweet:
    @classmethod
    def create(cls, user_id, tweet_text):
         # This will create a new tweet object,
         # and auto fill id
'''
from collections import defaultdict
class MiniTwitter:

    def __init__(self):
        # initialize your data structure here.
        self.time = 0
        self.user2Tweet = defaultdict(list)
        self.user2Friend = defaultdict(list)
        

    # @param {int} user_id
    # @param {str} tweet
    # @return {Tweet} a tweet
    def postTweet(self, user_id, tweet_text):
        # Write your code here
        tw = Tweet.create(user_id, tweet_text)
        self.user2Tweet[user_id].append((tw, self.time))
        self.time += 1
        return tw


    # @param {int} user_id
    # return {Tweet[]} 10 new feeds recently
    # and sort by timeline
    def getNewsFeed(self, user_id):
        # Write your code here
        ret = self.user2Tweet[user_id][-10:]
        for user in self.user2Friend[user_id]:
            ret.extend(self.user2Tweet[user][-10:])
        ret = sorted(ret, key=lambda x:x[1], reverse=True)
        return [i[0] for i in ret[:10]]

        
    # @param {int} user_id
    # return {Tweet[]} 10 new posts recently
    # and sort by timeline
    def getTimeline(self, user_id):
        # Write your code here
        return reversed([i[0] for i in self.user2Tweet[user_id][-10:]])
        

    # @param {int} from user_id
    # @param {int} to_user_id
    # from user_id follows to_user_id
    def follow(self, from_user_id, to_user_id):
        # Write your code here
        
        if to_user_id not in self.user2Friend[from_user_id]:
            self.user2Friend[from_user_id].append(to_user_id)
        

    # @param {int} from user_id
    # @param {int} to_user_id
    # from user_id unfollows to_user_id
    def unfollow(self, from_user_id, to_user_id):
        # Write your code here
        if to_user_id in self.user2Friend[from_user_id]:
            self.user2Friend[from_user_id].remove(to_user_id)