---
title: "Inactivity prediction to minimize customer churn for telecom"
categories:
  - Machine Learning
tags:
last_modified_at: 2022-01-13
image: 
  path: https://www.voxco.com/wp-content/uploads/2021/09/Everything-you-need-to-know-about-Customer-Churn1.jpg.webp
  thumbnail: https://www.voxco.com/wp-content/uploads/2021/09/Everything-you-need-to-know-about-Customer-Churn1.jpg.webp
---

Minimizing churn is one of the keys to success for a subscription media or commerce business. Loyal customers create predictable and compounding revenue for your business. If you can’t predict and prevent churn, you’ll spend a fortune trying to constantly acquire new users.

Machine Learning is empowering businesses to develop more forward-thinking retention strategies than ever before. As a result, subscription-driven companies use machine learning to predict and prevent customer churn.

## What is customer churn? ##

Customer churn (or customer attrition) is a tendency of customers to abandon a brand and stop being a paying client of a particular business. The percentage of customers that discontinue using a company’s products or services during a particular time period is called a customer churn (attrition) rate.Churn rate is a health indicator for businesses whose customers are subscribers and paying for services on a recurring basis.

There are many things brands may do wrong, from complicated onboarding when customers aren’t given easy-to-understand information about product usage and its capabilities to poor communication, e.g. the lack of feedback or delayed answers to queries. Another situation: Longtime clients may feel unappreciated because they don’t get as many bonuses as the new ones.In general, it’s the overall customer experience that defines brand perception and influences how customers recognize value for money of products or services they use.


## Use cases for customer churn prediction ##

As we mentioned before, churn rate is one of the critical performance indicators for subscription businesses. Let’s take a quick look at some companies with subscription business model:

**Music and video streaming services** are probably the most commonly associated with the subscription business model (Netflix, YouTube, Apple Music, Google Play, Spotify, Amazon Video, etc.).

**Media:** Digital presence is a must among the press, so news companies offer readers digital subscriptions besides print ones (Bloomberg, The Guardian, Financial Times, The New York Times, Medium etc.).

**Telecom companies (cable or wireless):** These companies may provide a full range of products and services, including wireless network, internet, TV, cell phone, and home phone services (AT&T, Sprint, Verizon, Cox Communications, etc.). Some specialize in mobile telecommunications (China Mobile, Vodafone, T-Mobile, etc.).

**Software as a service providers:** The adoption of cloud-hosted software is growing. According to Gartner, the SaaS market remains the largest segment of the cloud market. Its revenue is expected to grow 17.8 percent and reach $85.1 billion in 2019. The product range of SaaS providers is extensive: graphic and video editing (Adobe Creative Cloud, Canva), accounting (Sage 50cloud, FreshBooks), eCommerce (BigCommerce, Shopify), email marketing (MailChimp, Zoho Campaigns), and many others.

## Identifying at-risk customers with machine learning: ##

Companies that constantly monitor how people engage with products, encourage clients to share opinions, and solve their issues promptly have greater opportunities to maintain mutually beneficial client relationships.

And now imagine a company that has been gathering customer data for a while, so it can use it to identify behavior patterns of potential churners, segment these at-risk customers, and take appropriate actions to gain back their trust.Those following a proactive approach to customer churn management use predictive analytics. 

“The one weakness of tracking just real churn is that it serves only as a lagging indicator of poor customer experience, which is where a predictive churn model becomes extremely valuable.”

The main trait of machine learning is building systems capable of finding patterns in data, learning from it without explicit programming. In the context of customer churn prediction, these are behavior characteristics that indicate decreasing customer satisfaction from using company services/products.

To identifying potential churners, machine learning algorithms can do a great job here. They reveal some shared behavior patterns of those customers who have already left the company. Then, ML algorithms check the behavior of current customers against such patterns and signal if they discover potential churners.

Subscription-based businesses leverage ML for predictive analytics to find out which current users aren’t fully satisfied with their services and address their issues when it’s not too late.

## To-predict-churn-you-shouldnt-predict-churn. ##

For every subscription business, there exists a threshold of user inactivity after which it is very difficult, if not impossible, to win that user back. We have also found that building models to predict this point of inactivity yields more accurate leading indicators of churn than building models to predict actual churn itself.

Importantly, using inactivity as a proxy in our churn models still results in predicting true churn.

Inactivity and its Relationship to True Churn
We constructed a churn model using inactivity as the target label.We first wanted to validate that the inactivity prediction model accurately predicted true churn. The plot below validated this assumption.

Why is predicting using inactivity better than using actual cancellations?
We found that inactivity serves as a  better target label than actual churn, because the time a user actually cancels their subscription is a highly noisy variable (e.g. when they remember they have a subscription they are not using) while understanding a user’s engagement can be explicitly measured.

To demonstrate this phenomenon, the plot below examines the churn rate of a set of users as a function of the number of days of inactivity.

The plot shows that the rate of churn is fairly constant after 40 days of being inactive. In other words, once a user is inactive for 40 days it is merely a matter of chance when they will actually unsubscribe from the product. Thus training a model to predict whether a user will be inactive for 40 days can be a more accurate indicator of churn.




One of the initial steps in creating a predictive logistic regression model is to choose a period for for the independent variables , also called the predictors and the dependent or target variable. For that we need to define the observation and performance period window.

Observation Period

It is the period from where independent variables /predictors come from. In other words, the independent variables are created considering this particular period only. A period is also called a window.

Performance Period

This is the period from where dependent variable /target come from. It is the period following the observation window.


Therefore, in the current study, following Buckinx and Van
den Poel (2005), the time window of the data has been split into
two subperiods: a ‘‘calibration period’’ and a ‘‘prediction
period.’’ Consequently, an ‘‘inactive’’ customer is defined as
a customer who has been active during the calibration period
by having at least one purchase but shows no activity during the
prediction period.

splitting time for churn modeling purposes is not trivial
and involves certain challenges—such as duration of prediction
period.

. The difficulty being that prediction period duration
should be set in a way that it (1) captures activity/inactivity
of customers with a fairly long interpurchase time and (2) captures defection of those with a short average interpurchase time
as soon as possible

 To avoid the above-mentioned problems, the
duration of prediction period in this study is constructed in two
steps: (1) first, we sort customers in ascending order based on
their average interpurchase times and (2) the prediction period
is set to be approximately equal to the average interpurchase
time of the last customer in 99% mass of the sorted customer
base. This approach enables us to avoid prediction periods
being too long (and failing to detect churn long after it has happened), or too short (and misclassifying customers with relatively longer interpurchase time as ‘‘churners’’)

https://www.analyticsvidhya.com/blog/2020/10/the-complete-guide-to-checking-account-churn-prediction-in-bfsi-domain/
