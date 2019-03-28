# Stock price comparison using Ploylt-Dash

This data visulasition project is simple but complex enough to understand how to use ploylt and dash to build interactive web application. You can interact with the generated visulisation in [this link](https://stock-price-dash.herokuapp.com/). 

## Use the app: [https://stock-price-dash.herokuapp.com/](https://stock-price-dash.herokuapp.com/)

By checking the code of this application, you can learn the following topics.

1. How to use Dash
2. How to incorporate plotly graph object in Dash
3. How to make your graph interactive using a callback function
4. Working with Pandas dataframe
5. Converting a series into Pandas's datetime
6. Creating new column in a dataframe
7. Slicing a dataframe based on some conditions
8. Basic styling your web application

It shows two different plots. The scatter plot presents historical stock price comparison of three companies, Apple, Amazon and Google. You can choose what price you want to see using the radio buttons above the plot.

The other plot shows the volume of sales in different years. Again, you can choose a year (between 2015 to 2019) to play around.

A little note on how I publish the Python code in [Heroku](https://www.heroku.com/). If you do not have an account, first create an account. I am using the free tyre to publish my project. Then, follow this [guidline](https://dash.plot.ly/deployment). It says want you need to do step-by-step. I use GitHub as the repository. You can do it when you create the project in the Heroku website.

### Just remember the following topics.
1. Create an **virtual environment** to install dash and plotly or any other python packages. For mine I need to install Pandas. If you use your base environment, a lot of unnecessary packages will be installed in the Heroku server, which may cause problems, at least for free use.
2. I linked my GitHub repository with Heroku. Whenever you are done with some stable changes push those changes in the master branch of your git repository and then update the heroku too.

When you update your project, push it on the master branch of your git repository and then execute the following command in the command line (you need to download the Heroku Cli)

```
git push heroku master
```
It will rebuild the app in the Heroku server.

Enjoy!!!
