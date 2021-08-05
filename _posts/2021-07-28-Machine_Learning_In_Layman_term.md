---
title: "ML for Layman"
categories:
  - Machine Learning, Algorithm
tags:
last_modified_at: 2021-07-28
image: 
  path: https://images.unsplash.com/photo-1605027990121-cbae9e0642df?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1950&q=80
  thumbnail: https://images.pexels.com/photos/2599244/pexels-photo-2599244.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500 

---
https://www.quora.com/How-do-you-explain-Machine-Learning-and-Data-Mining-to-non-Computer-Science-people?top_ans=1866531 </br>
https://mlwhiz.com/blog/2017/02/05/ml_algorithms_for_data_scientist/ </br>
https://towardsdatascience.com/machine-learning-algorithms-in-laymans-terms-part-1-d0368d769a7b </br>
Mango Shopping

Suppose you go shopping for mangoes one day. The vendor has laid out a cart full of mangoes. You can handpick the mangoes, the vendor will weigh them, and you pay according to a fixed Rs per Kg rate (typical story in India).

Obviously, you want to pick the sweetest, most ripe mangoes for yourself (since you are paying by weight and not by quality). How do you choose the mangoes?

You remember your grandmother saying that bright yellow mangoes are sweeter than pale yellow ones. So you make a simple rule: pick only from the bright yellow mangoes. You check the color of the mangoes, pick the bright yellow ones, pay up, and return home. Happy ending?

Not quite.

Life is complicated

Suppose you go home and taste the mangoes. Some of them are not sweet as you'd like. You are worried. Apparently, your grandmother's wisdom is insufficient. There is more to mangoes than just color.

After a lot of pondering (and tasting different types of mangoes), you conclude that the bigger, bright yellow mangoes are guaranteed to be sweet, while the smaller, bright yellow mangoes are sweet only half the time (i.e. if you buy 100 bright yellow mangoes, out of which 50 are big in size and 50 are small, then the 50 big mangoes will all be sweet, while out of the 50 small ones, on average only 25 mangoes will turn out to be sweet).

You are happy with your findings, and you keep them in mind the next time you go mango shopping. But next time at the market, you see that your favorite vendor has gone out of town. You decide to buy from a different vendor, who supplies mangoes grown from a different part of the country. Now, you realize that the rule which you had learnt (that big, bright yellow mangoes are the sweetest) is no longer applicable. You have to learn from scratch. You taste a mango of each kind from this vendor, and realize that the small, pale yellow ones are in fact the sweetest of all.

Now, a distant cousin visits you from another city. You decide to treat her with mangoes. But she mentions that she doesn't care about the sweetness of a mango, she only wants the most juicy ones. Once again, you run your experiments, tasting all kinds of mangoes, and realizing that the softer ones are more juicy.

Now, you move to a different part of the world. Here, mangoes taste surprisingly different from your home country. You realize that the green mangoes are in fact tastier than the yellow ones.

You marry someone who hates mangoes. She loves apples instead. You go apple shopping. Now, all your accumulated knowledge about mangoes is worthless. You have to learn everything about the correlation between the physical characteristics and the taste of apples, by the same method of experimentation. You do it, because you love her.

Enter computer programs

Now, imagine that all this while, you were writing a computer program to help you choose your mangoes (or apples). You would write rules of the following kind:

if (color is bright yellow and size is big and sold by favorite vendor): mango is sweet.
if (soft): mango is juicy.
etc.

You would use these rules to choose the mangoes. You could even send your younger brother with this list of rules to buy the mangoes, and you would be assured that he will pick only the mangoes of your choice.

But every time you make a new observation from your experiments, you have to manually modify the list of rules. You have to understand the intricate details of all the factors affecting the quality of mangoes. If the problem gets complicated enough, it can get really difficult to make accurate rules by hand that cover all possible types of mangoes. Your research could earn you a PhD in Mango Science (if there is one).

But not everyone has that kind of time.

Enter Machine Learning algorithms

ML algorithms are an evolution over normal algorithms. They make your programs "smarter", by allowing them to automatically learn from the data you provide.

You take a randomly selected specimen of mangoes from the market (training data), make a table of all the physical characteristics of each mango, like color, size, shape, grown in which part of the country, sold by which vendor, etc (features), along with the sweetness, juicyness, ripeness of that mango (output variables). You feed this data to the machine learning algorithm (classification/regression), and it learns a model of the correlation between an average mango's physical characteristics, and its quality.

Next time you go to the market, you measure the characteristics of the mangoes on sale (test data), and feed it to the ML algorithm. It will use the model computed earlier to predict which mangoes are sweet, ripe and/or juicy. The algorithm may internally use rules similar to the rules you manually wrote earlier (for eg, a decision tree), or it may use something more involved, but you don't need to worry about that, to a large extent.

Voila, you can now shop for mangoes with great confidence, without worrying about the details of how to choose the best mangoes. And what's more, you can make your algorithm improve over time (reinforcement learning), so that it will improve its accuracy as it reads more training data, and modifies itself when it makes a wrong prediction. But the best part is, you can use the same algorithm to train different models, one each for predicting the quality of apples, oranges, bananas, grapes, cherries and watermelons, and keep all your loved ones happy :)

And that, is Machine Learning for you. Tell me if it isn't cool.

 

