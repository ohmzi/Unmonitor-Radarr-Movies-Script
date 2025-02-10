# Unmonitor-Radarr-Movies-Script
This script unmonitors new Plex movies in Radarr upon Tautulli detection, setting the movie’s status to 'False' and stopping future upgrades. Configure Tautulli’s 'Recently Added' to pass the movie title, and the script handles unmonitoring automatically.


---

## Table of Contents

1. [Features](#features)  
2. [Requirements](#requirements)  
3. [Installation & Configuration](#installation--configuration)
4. [How It Works](#how-it-works)
5. [Usage with Tautulli](#usage-with-tautulli)
6. [Testing](#testing)
7. [Troubleshooting](#troubleshooting)
8. [License](#license)

---

## Features

- **Automated Monitoring Management:** Automatically unmonitors a newly added movie in Radarr, ensuring Radarr does not continue to look for upgraded versions.  
- **Easy Integration with Tautulli:** Meant to be called from Tautulli’s notification system when a new movie is added to Plex.  
- **Simple Setup:** Works with minimal configuration—just add the necessary Radarr details (API URL and API Key) and set up a Tautulli notification agent.  

---

## Requirements

1. **Python 3** (and the [`requests`](https://pypi.org/project/requests/) library)  
   - Install via `pip install requests` if not already installed.  
2. **Radarr** (version 3 or newer)  
   - You need the Radarr API URL and an API key.  
3. **Tautulli**  
   - Configured to monitor Plex for Recently Added events.  
4. **Plex Media Server**  
   - Tautulli typically monitors Plex for new media additions.

---

## Installation & Configuration

1. **Clone or Download the Script**  
   - Save the script (e.g., `unmonitor_radarr.py`) to a directory accessible by Tautulli.

2. **Edit the Script**  
   - Update the following variables at the top of the script with your actual Radarr settings:
     ```python
     RADARR_API_URL = 'http://<IP_OF_YOUR_RADARR>:7878/api/v3/movie'
     RADARR_API_KEY = '<YOUR_RADARR_API_KEY>'
     ```
   
3. **Install Dependencies**  
   - Ensure `requests` is installed:
     ```bash
     pip install requests
     ```

---

## How It Works

- **Radarr API Call (GET Movies):**  
  The script first fetches a list of all movies from Radarr.  
- **Search for Match:**  
  It looks for a movie that matches the title passed from Tautulli.  
- **Unmonitor the Matched Movie:**  
  If it finds a match and that movie is monitored, it updates the `monitored` field to `False` via a Radarr `PUT` request.

---

## Usage with Tautulli

To have Tautulli automatically call your script when it detects a new file in Plex, follow these steps:

1. **Tautulli → Settings → Notification Agents**  
2. Click **Add a new notification agent** and choose **Script**.  
3. **Script Folder**: Browse to the folder where you stored this script (e.g., `/app` if that’s where `unmonitor_radarr.py` resides).  
4. **Script File**: Select the script file you want Tautulli to run (e.g., `unmonitor_radarr.py`).  
5. **Description**: Provide a friendly name (e.g., “Movie Unmonitoring Script”).  
6. **Trigger**: Choose **Recently Added** so that the script runs when a new movie is added to Plex.  
7. **Arguments**:  
   - Under **Recently Added** arguments, pass `"{title}"` (including quotes), so the script receives the movie’s title.  
   - Example:  
     ```bash
     python unmonitor_radarr.py "{title}"
     ```
8. **Save the Notification Agent**.

---

## Testing

1. **Run a Test Notification**:  
   - In Tautulli, click **Test** on the notification agent you just created.  
   - Select your script and provide a test movie name argument, e.g., `"Inception (2010)"`.  
   - This simulates a "movie added" event for "Inception (2010)."  
2. **Check Logs**:  
   - In Tautulli’s logs, verify that the script ran successfully.  
   - You should see output about whether the movie was found and whether it was unmonitored successfully.

---

## Troubleshooting

- **Script Fails to Run**:  
  - Ensure the script is executable (`chmod +x unmonitor_radarr.py` on Linux) or that your system is configured to execute `.py` files with Python by default.
- **Incorrect API URL or API Key**:  
  - Double-check you have the correct Radarr URL and API key in the script.  
  - If the script reports an error in fetching Radarr movies, verify that you can curl or wget the API endpoint with your API key.  
- **Movie Not Found in Radarr**:  
  - Confirm that Radarr is actually set to the correct naming/identification.  
  - The script does a simple case-insensitive match on the movie title.  
- **Still Monitored in Radarr**:  
  - Confirm no second instance of the same movie under a different quality profile or a different naming convention.

---


**Enjoy automatically unmonitoring movies in Radarr!** If you find this useful, consider sharing your setup or improvements with the community. If you run into any issues, feel free to open an issue or pull request.


---

## License

This project is provided “as is” without warranty of any kind. You are free to use, modify, and distribute this code as per the [MIT License](https://opensource.org/licenses/MIT).

---
