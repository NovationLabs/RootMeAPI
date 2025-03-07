# RootMe Stats API

#### Example JSON Response:
```json
{
  "totalChallenge": "594",
  "userChallenge": "11",
  "userName": "leo_gregori",
  "userPercent": "1%",
  "userRank": "130482",
  "userScore": "90"
}
```
📌 Using the API will return a JSON response with the user's Root-Me statistics.

## Usage:

### With curl:
```shell
curl "https://rootmeapi.vercel.app/api?username=leo_gregori"
```

### With python:
```python
import requests

url = "https://rootmeapi.vercel.app/api?username=leo_gregori"

data = requests.get(url).json()
print(data)
```
