from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from treelib import Node, Tree

class Articles(models.Model):
    title = models.CharField(max_length=250)
    content = models.CharField(max_length=250)

    def __str__(self):
        return self.title

   

    def getArticle(self):
        return Articles.objects.get(pk=self.id)


    def getTree(self):
        tree = Tree()
        commentList = Comments.objects.filter(articles_id=self.id).order_by('id')
        rootNode = Articles.objects.get(pk=self.id)
        tree.create_node(rootNode, 0)
        for i in commentList:
            print(i.id)
            #if i.parent_id==0:
                #tree.create_node(i.content,identifier=i.id, parent=i.parent_id)
            # print("id: ", i.id," parent_id: ", i.parent_id, " content: ", i.content)
            #else:
            tree.create_node(i.content, identifier=i.id, parent=i.parent_id)



class Comments(models.Model):
    content = models.CharField(max_length=250)
    articles_id = models.ForeignKey(Articles, on_delete=models.CASCADE)
    posted_time = models.DateTimeField(default=timezone.now)
    parent_id = models.IntegerField(db_index=True, default=0)
#    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.content




    
