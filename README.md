# hm-dates-api
This API provides you with the important dates and deadlines from the university of applied science munich in a convenient json format as well as an ical format.

## Usage
### Host on GitHub Pages
The API can be hosted on GitHub Pages and is updated via the GitHub Actions script:"static.yml" every day at 02:00 UTC.
### Host on your own server
You can host the API on your own server. Just use the provided docker image to tun it on your server.
The docker image similarly updates the data every day at 02:00 UTC.
Be careful the docker does not provide a webserver. You have to use a webserver like nginx to provide the API via HTTP.
You can use the example docker-compose.yml to run the API Container on your server.

## API
The data is available for the current and the next semester, to get the data for the current semester you have to send a GET request to the API with the path dates-api/thissemester/... \
To get the data for the next semester you have to send a GET request to the API with the path dates-api/nextsemester/...
Example for a GET request to get all the data for the current semester:
```http
GET https://YOURDOMAIN/dates-api/thissemester/all.json
```
The Attributes of the JSON are: For example for the Event lecture_free_period:
```json
{
    "title": "Vorlesungsfreie Zeit",
    "dates": [
        {
            "start": "2023-04-06T00:00:00",
            "end": "2023-04-11T23:59:59"
        },
        {
            "start": "2023-05-26T00:00:00",
            "end": "2023-05-30T23:59:59"
        },
        {
            "start": "2023-07-08T00:00:00",
            "end": "2023-09-30T23:59:59"
        }
    ],
    "tag": "lecture_free_time"
}
```

As an Example 

1. title (string): The title or name of the Event. It's the same as the title on the website. 

2. dates (array): An array of objects representing individual periods of lecture-free time. Each object has two attributes, "start" and "end," specifying the start and end dates and times for the period.

   * start (string): The start date and time of the lecture-free period in ISO 8601 format (YYYY-MM-DDTHH:MM:SS). The time is set to 00:00:00 for the start of the day.

   * end (string): The end date and time of the lecture-free period in ISO 8601 format (YYYY-MM-DDTHH:MM:SS). The time is set to 23:59:59 for the end of the day.

3. tag (string): A tag or label associated with the event, these are static identifiers 

You can also get the data for a specific tag (note: only the events with a tag and "recent_data" as well as "time_of_last_update" are provided separately). \
To do this you have to send a GET request to the API with the path dates-api/THESEMESTER/TAG.json \
If the python fails at getting the data from the website it will set the "recent_data" flag in the json to false and exit the program.
## Ical
The API also provides you with the data for the current semester in an ical format.
To get the data for the current semester you have to send a GET request to the API with the path dates-api/ical/calendar.ics