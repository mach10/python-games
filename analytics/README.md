#Analytics Caching

There is a long running query that grabs Music Analytics data from a data warehouse for a dashboard report.
Our data pipeline updates this data once an hour, at 20 after the hour. When a query pulls this data we want to cache
it as long as the data warehouse has not been updated. 

Write a function that calculates how long in seconds from the
current time that this data should be stored so that it expires exactly when it is next updated.