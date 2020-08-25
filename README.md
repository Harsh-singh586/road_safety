# road_safety
Road safety is an API developed using Django.


First type of API call

    sample url to call an API main/date-time/url

    Date should be of format 'YYYY - MM - DD'

    Time should be of format 'Hours - Minutes' 24- hour Format

    Date and time should be of seperated by + sign
        Example : main/2020-08-24+20:01/myevent
        response: [{ "url": "myevent", "date_time": "2020-08-24 20:01" }]

    If Date - Time parameter of API call matches with current Date - time it will return status 204

Adding a record

    We can add a record in DB at main/add
    url - date/time pair should be unique

Ping

    API can be ping from main/ping
    If server is running it will return {'status' : 'ok'} 


