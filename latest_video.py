import os
import pickle
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
import re
import datetime

scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]

def get_authenticated_service(name):
    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "Byte Comic.json"
    credentials_file = f"Files/{name}.pickle"

    # Load or obtain credentials
    if os.path.exists(credentials_file):
        with open(credentials_file, 'rb') as token:
            credentials = pickle.load(token)
    else:
        flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
            client_secrets_file, scopes)
        credentials = flow.run_local_server(port=0)
        with open(credentials_file, 'wb') as token:
            pickle.dump(credentials, token)

    # Build the service
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

    return youtube

def parse_duration(duration_str):
    match = re.match(r'PT(\d+H)?(\d+M)?(\d+S)?', duration_str)
    if not match:
        return None

    hours = int(match.group(1)[:-1]) if match.group(1) else 0
    minutes = int(match.group(2)[:-1]) if match.group(2) else 0
    seconds = int(match.group(3)[:-1]) if match.group(3) else 0

    return datetime.time(hour=hours, minute=minutes, second=seconds)

def get_latest_video_details(name,channel_id):
    # Get authenticated service
    service = get_authenticated_service(name)

    # Retrieve uploads playlist ID
    channel_request = service.channels().list(
        part='contentDetails',
        id=channel_id
    )
    channel_response = channel_request.execute()
    uploads_playlist_id = channel_response['items'][0]['contentDetails']['relatedPlaylists']['uploads']

    # Retrieve playlist items
    playlist_request = service.playlistItems().list(
        part='snippet',
        playlistId=uploads_playlist_id,
        maxResults=1  # Retrieve only the latest video
    )
    playlist_response = playlist_request.execute()

    # Extract latest video
    latest_video = playlist_response['items'][0]

    # Access video details
    video_id = latest_video['snippet']['resourceId']['videoId']
    video_title = latest_video['snippet']['title']
    video_description = latest_video['snippet']['description']
    video_thumbnail_url = latest_video['snippet']['thumbnails']['default']['url']

    # Get video duration
    video_request = service.videos().list(
        part="contentDetails",
        id=video_id
    )
    video_response = video_request.execute()
    video_duration = video_response['items'][0]['contentDetails']['duration']
    
    # Parse and format duration
    formatted_duration = parse_duration(video_duration).strftime('%H:%M:%S')

    video_details = {
        "video_id": video_id,
        "video_title": video_title,
        "video_description": video_description,
        "video_thumbnail_url": video_thumbnail_url,
        "video_duration": formatted_duration,
        "video_watch_url": f"https://www.youtube.com/watch?v={video_id}"
    }

    return video_details

# Example usage:
# channel_id = "UCfjQOWJqoQ69BUaUZtFtGZg"
# latest_video_details = get_latest_video_details(channel_id)

# # Access individual details
# print("Latest Video Details:")
# print("Video ID:", latest_video_details["video_id"])
# print("Title:", latest_video_details["video_title"])
# print("Description:", latest_video_details["video_description"])
# print("Thumbnail URL:", latest_video_details["video_thumbnail_url"])
# print("Duration:", latest_video_details["video_duration"])
# print("Watch URL:", latest_video_details["video_watch_url"])
