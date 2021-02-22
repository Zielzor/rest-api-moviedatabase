# data comes from https://developers.themoviedb.org/3/getting-started/introduction
import requests
import pprint
import pandas as pd

APIv3 = "18863b8a96c6dc619fbb00166fbd2d61"
APIv4 = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIxODg2M2I4YTk2YzZkYzYxOWZiYjAwMTY2ZmJkMmQ2MSIsInN1YiI6IjYwMzNkNzJmN2Q1ZjRiMDA" \
        "0MTk4Yjg1YSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.OYG8p6QhqovqbZs3nKi6_aOBpE94UJRIT7VOVurHq8s"

# internet connection request
# endpoint(url from where to grab data)
# HTTP method

'''
GET - method
/movie/{movie_id} - path/endopoint
https://api.themoviedb.org/3/movie/550?api_key=18863b8a96c6dc619fbb00166fbd2d61  - example request , the "3" is the 
api version
'''
# Using v4 , using bearer token 
movie_id = 501
api_version = 4
api_base_url = f"https://api.themoviedb.org/{api_version}"
endpoint_path = f"/movie/{movie_id}"
endpoint_V4 = f"{api_base_url}{endpoint_path}"
headers = {
    'Authorization': f'Bearer {APIv4}',
    'Content-Type': 'application/json;charset=utf-8'
}
# r = requests.get(endpoint_v4, headers=headers) # json={"api_key": api_key})
# print(r.status_code)
# print(r.text)

# using v3
movie_id = 500
api_version = 3
api_base_url = f"https://api.themoviedb.org/{api_version}"
endpoint_path = f"/search/movie"
search_query = "Batman"
endpoint = f"{api_base_url}{endpoint_path}?api_key={APIv3}&query={search_query}"

r = requests.get(endpoint)
if r.status_code in range(200, 299):
    data = r.json()
    results = data["results"]
    if len(results) > 0:
        movie_ids = set()
        for result in results:
            _id = result["id"]
            print(result["title"], _id)
            movie_ids.add(_id)
        print(movie_ids)

output = "movies.csv"
movie_list = []
for movie_id in movie_ids:
    api_version = 3
    api_base_url = f"https://api.themoviedb.org/{api_version}"
    endpoint_path = f"/movie/{movie_id}"
    endpoint = f"{api_base_url}{endpoint_path}?api_key={APIv3}"
    r = requests.get(endpoint)
    if r.status_code in range(200, 299):
        data = r.json()
        movie_list.append(data)


df = pd.DataFrame(movie_list)
df.to_csv(output, index=False)


