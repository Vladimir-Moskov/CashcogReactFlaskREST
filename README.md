# Home work for XCNT GmbH

Hi Volodymyr,

Great that you're still interested! As a next step in the interview process we would like you to solve our coding challenge.

I hope you have fun and should there be any questions, don’t hesitate to contact me.
It would be great if you could solve these two tasks until 6th of January 2020.

Background:
Even in the world of startups and company builders expenses for trips etc. have to be filed and managed.
The fictitious expense software Cashcog tries to manage this. Unfortunately, there is some functionality missing which you have to create.
The Cashcog-API only offers events about newly created expenses. The approval process however is missing and has to be added externally.

The Cashcog system provides the following endpoints to push out newly created expenses.
They are randomly generated and occur at a random interval.

Cashcog event stream API-Endpoint:
https://cashcog.xcnt.io/stream

For testing purposes the following API-Endpoint can be used to fetch a single expense object.
https://cashcog.xcnt.io/single

Cashcog expense example event:
{
"uuid": "92b19fc6-5386-4985-bf5c-dc56c903dd23",
"description": "Itaque fugiat repellendus velit deserunt praesentium.",
"created_at": "2019-09-22T23:07:01",
"amount": 2291,
"currency": "UZS",
"employee": {
"uuid": "858142ac-299a-48f0-b221-7d6de9439454",
"first_name": "Birthe",
"last_name": “Meier"
}
}

Part 1 – BE-Part
Consume the expense events provided by the Cashcog Expense-API. Validate and store them in a database of your choice.
Create a Graph-QL or RESTful-API which allows clients to fetch, update (approve or decline), and query these expenses.

Part 2 – FE-Part
Visualize the approval process in a web application. The user should be able to get all expenses from the BE system, query/filter
and sort them, and approve or decline them. Create an UI which is intuitive and responsive so it works on both, desktop and mobile platforms.

After completing the assignment please provide me with your source-code on an accessible git repository.

Best Regards,


