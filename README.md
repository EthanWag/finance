# Personal and Business finance tracker

## Introduction
The purpose of this application is to be a user friendly finance tool used to help people and small business keep track of their finances. Designed to work well with beginners and experts with keeping track of their finances and in the future, provide them with the tools they need to design and keep track of budgets. It's going to very customizable with a brand new account being easy to navigate and understand but will have the ability to install plugins customize your experience depending on your skill level.
  
In the future (If I ever even get to it) it will have AI agents to be able to give advise on how to design a budget and for research purposes, will be able to help research companies and will provide anaylitical insight using data collected off of edgar. In the end, I expect this to look more like a framework in which people can build and use financial tools.

## Tech Stack
The frontend will mostly be written in React and typescript and take advantage of tools like bootstrap in order to have a nice clean design. It might be benefical to work some other frameworks, but that will require lots of research but would allow for customizability.

The backend for the API would most likely use python as much of this application will benefit greatly from pythons libraries. Likewise, using python leaves the door for integration with AI which is something later down the line as something I would like to mess around with

Finally for a database the would most likely be used for the backend, I would like to use MongoDB to take advantage of cloud storage but I would also want to design it in such a way to change out databases. For example, for some features, it may be helpful to use neo4j for features that require a graph data structure to them. However for keeping track of usernames and passwords, as well as any other misc blob objects would work great in mongodb.

## Design

Well as for right now, I would like to design the database in such a way that a user would have access to personal budgets and tools they have made but if the user wanted to, they could tie their personal account with a business account(s) and have the ability to share that with other people. With a business account, you would have access to different tools that would be more tailored to a business needs. You would be able to colab with other users in conducting research and being able share verious notes and insights. 

Inside of a business account you would also have access to forcasting abilities and with AI integration, you would be able to get helpful insights on how you can save money and use your assets wisely

![drawSQL-image-export-2025-04-17](https://github.com/user-attachments/assets/2b3e5216-5562-4972-965b-f1e0e5289831)

## Features

I thought it might be kinda nice to get notifications on your phone reminding you to enter in your budget for the week/timeperiod. The user would control when they want to be notified and the application would hold them to goal they set and would help them draft ideas on how to keep their budget.
