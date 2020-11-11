import os 
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "learning_log.settings") ## (always same, name of project (not app))

import django
django.setup()

from learning_logs.models import Topic
topics = Topic.objects.all() ## kind of like select * from Topic, getting everything in the Topic model

for topic in topics:
    print("Topic ID:", topic.id," ->  Topic:", topic)


t = Topic.objects.get(id=1) ## returns one particular row (kind of like a select where)
print(t) 
print(t.date_added)

entries = t.entry_set.all() ## don't have to import entries because there is a FK relationship between entry and topic
for entry in entries:
    print(entry) ## will have to comment out the truncation setting in models.py to see the whole text, no way to do this in print() 

