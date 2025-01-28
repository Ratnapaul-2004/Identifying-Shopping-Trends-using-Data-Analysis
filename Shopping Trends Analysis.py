#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install WordCloud')


# In[2]:


import numpy as np 
import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt 
import plotly.express as px 


# In[5]:


shop = pd.read_csv('C:/Users/user/Downloads/shopping_trends_updated1.csv')


# In[17]:


shop.shape


# In[6]:


shop.to_excel('shopping_trends_updated1.xlsx')


# In[20]:


shop.head()


# In[21]:


shop.dtypes


# In[22]:


shop.columns


# In[23]:


shop.info()


# In[24]:


shop.shape


# In[25]:


shop.isnull().sum()


# In[26]:


print(f"The unique values of the 'Gender' column are: {shop['Gender'].unique()}")
print()
print(f"The unique values of the 'Category' column are: {shop['Category'].unique()}")
print()
print(f"The unique values of the 'Size' column are: {shop['Size'].unique()}")
print()
print(f"The unique values of the 'Subscription Status' column are: {shop['Subscription Status'].unique()}")
print()
print(f"The unique values of the 'Shipping Type' column are: {shop['Shipping Type'].unique()}")
print()
print(f"The unique values of the 'Discount Applied' column are: {shop['Discount Applied'].unique()}")
print()
print(f"The unique values of the 'Promo Code Used' column are: {shop['Promo Code Used'].unique()}")
print()
print(f"The unique values of the 'Payment Method' column are: {shop['Payment Method'].unique()}")


# # Upon initial observation, we have seen that it is a comprehensive and well -structured dataset with 3900 rows and 18 columns. Now we can start our data analysis journey

# # 1. What is the overall distribution of customer ages in the dataset?

# In[27]:


shop['Age'].value_counts()


# In[28]:


shop['Age'].mean()


# In[29]:


shop['Gender'].unique()


# In[30]:


shop['Age_category'] = pd.cut(shop['Age'], bins= [0,15, 18 , 30 , 50 , 70] , labels= ['child' , 'teen' , 'Young Adults' ,'Middle-Aged Adults'
                                                                                             , 'old'] )


# In[31]:


fig = px.histogram(shop , y = 'Age' , x = 'Age_category')
fig.show()


# # 2. How does the average purchase amount vary across different product categories?

# In[32]:


shop.columns


# In[33]:


shop['Category'].unique()


# In[34]:


shop.groupby('Category')['Purchase Amount (USD)'].mean()


# # 3. which gender has the highest number of purchases?

# In[35]:


shop.columns


# In[36]:


sns.barplot(shop , x = 'Gender' , y = 'Purchase Amount (USD)')


# # 4. What are the most commonly purchased items in each category?

# In[37]:


shop.columns


# In[38]:


shop.groupby('Category')['Item Purchased'].value_counts()


# In[39]:


fig = px.histogram(shop , x = 'Item Purchased' , color = 'Category')
fig.show()


# # 5. Are there any specific seasons or months where customer spending is significantly higher?

# In[40]:


shop['Season'].unique()


# In[41]:


shop[shop['Season'] == 'Summer'].value_counts().sum()


# In[42]:


shop[shop['Season'] == 'Winter'].value_counts().sum()


# In[43]:


shop[shop['Season'] == 'Spring'].value_counts().sum()


# In[45]:


shop[shop['Season'] == 'Fall'].value_counts().sum()


# In[46]:


fig = px.histogram(shop , x = 'Season' , range_y= [200 , 1500] )
fig.show()


# # 6. What is the average rating given by customers for each product category?

# In[47]:


shop_groupby = shop.groupby('Category')['Review Rating'].mean().reset_index()


# In[48]:


fig = px.bar(shop_groupby ,x= 'Category' , y = 'Review Rating' )
fig.show()


# # 7. Are there any notable differences in purchase behavior between subscribed and non-subscribed customers?

# In[10]:


shop.columns


# In[11]:


shop['Subscription Status'].unique()


# In[15]:


sns.barplot(shop  , x = 'Subscription Status' , y = 'Purchase Amount (USD)')


# In[16]:


shop['Purchase Amount (USD)'].sum()


# In[17]:


shop.groupby('Subscription Status')['Purchase Amount (USD)'].mean()


# # 8. Which payment method is the most popular among customers?

# In[18]:


shop.groupby('Payment Method')['Purchase Amount (USD)'].mean().sort_values(ascending= False)


# In[20]:


shop_groupby = shop.groupby('Payment Method')['Purchase Amount (USD)'].mean().reset_index()


# In[23]:


fig = px.bar(shop_groupby , x = 'Payment Method' , y = 'Purchase Amount (USD)')
fig.show()


# In[24]:


sns.barplot(shop ,x='Payment Method' , y = 'Purchase Amount (USD)')


# # 9. Do customers who use promo codes tend to spend more than those who don't?

# In[25]:


shop_groupby  = shop.groupby('Promo Code Used')['Purchase Amount (USD)'].sum().reset_index()


# In[26]:


fig = px.sunburst(shop , path=['Gender' , 'Promo Code Used'] , values='Purchase Amount (USD)')
fig.show()


# In[27]:


fig  =  px.bar(shop_groupby , x= 'Promo Code Used' , y = 'Purchase Amount (USD)')
fig.show()


# # 10. How does the frequency of purchases vary across different age groups?

# In[8]:


shop.columns


# In[9]:


age_bins = [0, 18, 35, 55, 65]
age_labels = ['Teen Agers', 'Young Adults', 'Middle-aged Adults', 'Old']


# In[10]:


shop['Age_category'] = pd.cut(shop['Age'], bins=age_bins, labels=age_labels, right=False)
shop[['Age' , 'Age_category']]


# In[11]:


shop['Age_category'].unique()


# In[12]:


shop_group = shop.groupby('Frequency of Purchases')['Age'].sum()


# In[41]:


px.sunburst(shop , path=['Frequency of Purchases','Age'] , values='Age')


# # 11. Are there any correlations between the size of the product and the purchase amount?

# In[15]:


shop.columns


# In[16]:


shop_group = shop.groupby('Size')['Purchase Amount (USD)'].sum().reset_index()


# In[17]:


fig  = px.bar(shop_group , x = 'Size' , y ='Purchase Amount (USD)'  )
fig.show()


# # 12. Which shipping type is preferred by customers for different product categories?

# In[18]:


shop.groupby('Category')['Shipping Type'].value_counts().sort_values(ascending= False)


# In[19]:


shop['Shipping_Category'] =shop['Shipping Type'].map({'Express': 0, 'Free Shipping': 1, 'Next Day Air': 2,
                                                       'Standard': 3, '2-Day Shipping': 4, 'Store Pickup': 5})


# In[20]:


shop['Category'].unique()


# In[22]:


shop['Category_num'] =shop['Category'].map({'Clothing':1, 'Footwear':2, 'Outerwear':3, 'Accessories':4})


# # 13. How does the presence of a discount affect the purchase decision of customers?

# In[23]:


shop.columns


# In[24]:


shop_group = shop.groupby('Discount Applied')['Purchase Amount (USD)'].sum().reset_index()


# In[25]:


px.histogram(shop_group , x = 'Discount Applied' , y = 'Purchase Amount (USD)')


# In[26]:


fig = px.sunburst(shop , path = ['Gender' , 'Discount Applied'], values='Purchase Amount (USD)' , color= 'Gender')

fig.show()


# # 14. Are there any specific colors that are more popular among customers?

# In[27]:


px.histogram(shop , x = 'Color')


# In[28]:


shop['Color'].value_counts().nlargest(5)


# # 15. What is the average number of previous purchases made by customers?

# In[29]:


shop['Previous Purchases'].mean()


# # 16. Are there any noticeable differences in purchase behavior between different locations?

# In[30]:


shop.groupby('Location')['Purchase Amount (USD)'].mean().sort_values(ascending = False)


# In[31]:


shop_group = shop.groupby('Location')['Purchase Amount (USD)'].mean().reset_index()


# In[32]:


fig = px.bar(shop_group, x = 'Location' , y = 'Purchase Amount (USD)')
fig.show()


# # 17. Is there a relationship between customer age and the category of products they purchase?

# In[33]:


shop_group = shop.groupby('Category')['Age'].mean().reset_index()


# In[34]:


fig = px.bar(shop_group ,y = 'Age' , x= 'Category')
fig.show()


# # 18. How does the average purchase amount differ between male and female customers?

# In[35]:


shop_group = shop.groupby('Gender')['Purchase Amount (USD)'].sum().reset_index()


# In[36]:


fig = px.bar(shop_group , x = 'Gender' , y = 'Purchase Amount (USD)')
fig.show()


# In[42]:


px.sunburst(data_frame= shop , path = ['Gender' ,'Age'] , values='Purchase Amount (USD)')

