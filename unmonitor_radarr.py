import requests
import sys

# Radarr API settings
RADARR_API_URL = 'http://0.0.0.0:7878/api/v3/movie'
RADARR_API_KEY = 'RADARR_API_KEY'

def unmonitor_movie(movie_title):
    # Fetch all movies from Radarr
    response = requests.get(
        RADARR_API_URL,
        headers={'X-Api-Key': RADARR_API_KEY}
    )

    if response.status_code != 200:
        print(f"Error fetching movies from Radarr: {response.status_code} - {response.text}")
        return

    radarr_movies = response.json()

    # Find the movie and unmonitor it
    for movie in radarr_movies:
        if movie['title'].lower() == movie_title.lower() and movie['monitored']:
            print(f"Found movie '{movie_title}' in Radarr. Attempting to unmonitor...")
            movie['monitored'] = False
            update_response = requests.put(
                f"{RADARR_API_URL}/{movie['id']}",
                headers={'X-Api-Key': RADARR_API_KEY},
                json=movie
            )
            if update_response.status_code == 200:
                print(f"Successfully unmonitored '{movie_title}' in Radarr.")
            else:
                print(f"Failed to update movie: {update_response.status_code}")
            return

    print(f"Movie '{movie_title}' not found or already unmonitored.")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        movie_title = sys.argv[1]
        unmonitor_movie(movie_title)
    else:
        print("No movie title provided.")
