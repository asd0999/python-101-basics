headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"]
news_ticker = ""
# TODO: set news_ticker to a string that contains no more than 140 characters long.
# HINT: modify the headlines list to verify your loop works with different inputs

for headline in headlines:
    if len(news_ticker + headline) >= 140:
        break
    else:
        news_ticker = news_ticker + headline + "/"

#print(len(news_ticker))

x = 140-len(news_ticker)
y = headline[:x]
print(x,y)

news_ticker = news_ticker + str(y)

print(news_ticker)
print(len(news_ticker))

'''
EASIER WAY TO DO THIS
for headline in headlines:
    news_ticker += headline + "/"
    if len(news_ticker) >= 140:
        news_ticker = news_ticker[:140]
        break
print(news_ticker)
'''
