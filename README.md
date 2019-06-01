# unveiled-inception-worker
This project aims to isolate the inceptionv3 worker from [unveiled-deep-app](https://github.com/greyzor/unveiled-deep-app)

## Description
Inceptionv3 is the denomination for state of the art the learning architecture, pre-trained to recognize content in images (using imagenet dataset).

## Preview
A demo of the api is hosted on heroku: [unveiled-app.herokuapp.com/](https://unveiled-app.herokuapp.com/) , or using a web client:
```console
# Api Status
curl -XGET https://unveiled-inception-worker-api.herokuapp.com/api/1/status
```
This would result in:
```json
{ "status": "ok" }
```
```console
# Classify a file image: replace <YOUR_FILE> by the corresponding local path.
curl --data-binary @<YOUR_FILE> -XPOST http://localhost:5000/api/1/classify
```
Which would for return you most probable classes with associated confidence scores.
```json
{
  "results": [
    [
      "n07920052",
      "espresso",
      "0.74209744"
    ],
    [
      "n02823750",
      "beer_glass",
      "0.08886051"
    ]
  ],
  "status": "done",
  "timing": 4.967261791229248
}
```

## Development
```
# Install packages
python3 -m pip install -r requirements.txt

# Run the server locally (default port: 5000)
python3 manage.py run
```

## Limitations
The currently hosted preview has limitations in terms of memory. It may sometimes be idle or unavailable due to automatic heroku restart (memory quota exceeded).

## Contributions
Please feel free to fork this project or directly pull requests for additional features.
You're also welcome to contribute to the mother project: [unveiled-deep-app](https://github.com/greyzor/unveiled-deep-app)