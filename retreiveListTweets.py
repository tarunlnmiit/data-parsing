from twitter import *

t = Twitter(auth=OAuth('1100686363-6JxQIno5T8UMPQeWyaH783qrxxJJrmwbLJCEtoF', 'GqgnME3MRfOQL79TzWuH5S9fJOgXXogdAwyVDzGSk4ovD', 'mDkejxEBQYTj99RNkYhc1mCTE', 'WR2xlMAu4gRelaPRDkywDXCAGldZOZT6u4AymUBE0MpyjtooCg'))

# Retrieval of list of tweets to a certain user
pythonStatuses = t.statuses.user_timeline(screen_name='i_tarun_gupta', count=5)
print pythonStatuses