from html.parser import HTMLParser

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print ("Start :", tag)
        if  attrs != []:
            
            for i,j in attrs:
                 print("->",i,">",j)
    def handle_endtag(self, tag):
        print ("End   :", tag)
    def handle_startendtag(self, tag, attrs):
        print ("Empty :", tag)
        if  attrs != []:
            
            for i,j in attrs:
                 print("->",i,">",j)        
import re
n=int(input())
parser=MyHTMLParser()
for i in range(n):
    parser.feed(input())  
