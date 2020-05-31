### Trace User Actions

TraceUserActions contains app **UserActions** which deals with storing the user activities over an application.

UserActions.models contains two models.
* UserTimeZone - An extension to User model to store user timezone information
* ActivityPeriod - contains user activity timings 

To insert sample data into the database, we can use the custom command 'insertdata'.
This will insert 10 users to Users table and three records per user in ActivityPeriod Table.
After saving the user object in User model, by using the post save signal, random timezone is assigned to each user and this information is stored in UserTimeZone model.

As there will be different timezones for every user, the activity timings will be stored in UTC timezone.
While retrieving the data from database, utc time will be converted to corresponding timezone.

*Heroku app url - https://trace-user-actions.herokuapp.com/*

**Admin Login:**
username / password - root_user / Welcome@2020

**Activity period API:** https://trace-user-actions.herokuapp.com/activity/

By default, the above url will return the UTC datetime. 

In order to get normalized datetimes (datetime corresponding to user timezones), pass the query param 'utc' with a value False.

https://trace-user-actions.herokuapp.com/activity/?utc=False
