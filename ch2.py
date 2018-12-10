# -*-coding: utf-8 -*-

paragraph = '''
Most discussions of GraphQL focus on data fetching, but any complete data platform needs a way to modify server-side data as well.
In REST, any request might end up causing some side-effects on the server, but by convention it's suggested that one doesn't use GET requests to modify data. GraphQL is similar - technically any query could be implemented to cause a data write. However, it's useful to establish a convention that any operations that cause writes should be sent explicitly via a mutation.
Just like in queries, if the mutation field returns an object type, you can ask for nested fields. This can be useful for fetching the new state of an object after an update.
'''

# Q1
print('Q1:段落長度', len(paragraph))

# Q2
lowertext = paragraph.lower()
replacetext = lowertext.replace('graphql','GRAPHQL')
print('Q2:文字替換',replacetext)

# Q3
vocabulary = paragraph.split()
print('Q3:字數總數', len(vocabulary))

# Q4
x = 1; y = 6
x = (y-x)+x
y = x // y
print('Q4:x =', x, 'y =', y)




