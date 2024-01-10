'''
SourceAcquiredBOT.py
Read r/SauceSharingCommunity comments and search for any kind of approved hyperlinks (or) !solved keyword. 
If found, make post flair 'Source acquired'
'''

import praw, re, traceback
import reprocess

#Reddit connection
reddit = praw.Reddit(user_agent="YourUserAgent",
                     client_id="YourClientID",
                     client_secret="YourClientSecret",
                     username="YourUserName",
                     password="YourPassword")

#Select subreddit to process
subreddit = reddit.subreddit('SauceSharingCommunity')

saucereqflair   = 'YourSourceRequiredFlairID'
sauceacqflair   = 'YourSourceAcquiredFlairID'

#Keyphrase to trigger the BOT
keyphrase       = '!solved'

reprocess_keyphrase  =  '!reprocess'

#Links to trigger the BOT
sources = ['anidb', 'anime', 'artstation', 'book', 'booru', 'chan', 'comic', 'cubari', 'danke', 'deviantart', 'doujin', 'e621', 'fakku', 'hbrowse', 'hentai', 'hiperdex', 'hitomi', 'instagram', 'jav', 'livechart', 'manga', 'nijie', 'patreon', 'pixiv', 'porn', 'r18', 'reddit', 'rule34', 'sankaku', 'tsumino', 'twitter', 'yande', '8muses', 'toonily', 'webtoon', 'bato.to', 'newgrounds', 'novel', 'nana.my.id']

#User blacklist
userBlacklist = ['AutoModerator', 'SauceSharingBOT', 'RemindMeBot', 'RepostSleuthBot', 'TheReposterminator', 'Flair_Helper', 'FloodgatesBot', 'sneakpeekbot']

#URLs blacklist
urlBlacklist  = ['https://www.reddit.com/r/saucesharingcommunity/wiki/index)', 
                 'https://www.reddit.com/r/saucesharingcommunity/wiki/index).', 
                 'https://www.reddit.com/r/saucesharingcommunity/wiki/index/)', 
                 'https://www.reddit.com/r/saucesharingcommunity/wiki/index/).', 
                 'https://www.reddit.com/r/saucesharingcommunity/wiki/index/rules)',  
                 'https://www.reddit.com/r/saucesharingcommunity/wiki/index/rules).',
                 'https://www.reddit.com/r/saucesharingcommunity/wiki/index/rules/)',  
                 'https://www.reddit.com/r/saucesharingcommunity/wiki/index/rules/).',
                 'https://www.reddit.com/r/saucesharingcommunity/new)', 
                 'https://www.reddit.com/r/saucesharingcommunity/new).', 
                 'https://www.reddit.com/r/saucesharingcommunity/new/)', 
                 'https://www.reddit.com/r/saucesharingcommunity/new/).', 
                 'https://play.google.com/store/apps/details?id=com.reddit.frontpage)', 
                 'https://play.google.com/store/apps/details?id=com.reddit.frontpage).', 
                 'https://www.reddit.com/r/saucesharingcommunity/submit?url=)',
                 'https://www.reddit.com/r/saucesharingcommunity/submit?url=).',                 
                 'https://www.reddit.com/r/saucesharingcommunity/submit)',
                 'https://www.reddit.com/r/saucesharingcommunity/submit).',
                 'https://www.reddit.com/r/SauceSharingCommunity/wiki/index/rules/#wiki_rule_.236.3A_use_saucenao.)', 
                 'https://saucenao.com/)']

def processURL(submission, comment):
    """ Process URL, if criteria met, make 'Source acquired' """
    try:
        #Get all URLs from the comment body
        urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', comment.body)
        if (len(urls) > 0) and comment.author not in userBlacklist and submission.link_flair_template_id == saucereqflair:
            for u in urls:
                if u in urlBlacklist:
                    continue
                for s in sources:
                    if (u.find(s) > 0):
                        submission.flair.select(sauceacqflair)
                        print('Flair changed!', flush = True)
                        return
    except:
        traceback.print_exc()

if __name__ == "__main__":
    # ------------------------------------#
    # Loop the comments stream until the Reddit access token expires.
    # Then get a new access token and start the stream again.
    while 1:
        try:
            for comment in subreddit.stream.comments(pause_after=0):
                if comment:
                    submission = comment.submission
                    comment.body = comment.body.lower()
                    
                    print("Processing comment: \t reddit.com{}".format(comment.permalink), flush = True)
                    
                    #If not flaired then you flair
                    if (hasattr(submission, 'link_flair_template_id') == False):
                        submission.flair.select(saucereqflair)
                    
                    #Process Keyphrase
                    if keyphrase in comment.body:
                        if submission.link_flair_template_id == saucereqflair:
                            submission.flair.select(sauceacqflair)
                            print('Flair changed!', flush = True)
                        continue
                    
                    #Process reprocess_keyphrase
                    if reprocess_keyphrase in comment.body:
                        if submission.link_flair_template_id == saucereqflair:
                            reprocess.reprocess_Submission(comment, submission)
                            print('Reprocessed!', flush = True)
                        continue
                    
                    processURL(submission, comment)
        except Exception as e:
            traceback.print_exc()
