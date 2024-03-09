# Coded by Eddie's Tech (eddiestech.co.uk) - Adapted from YouTube API example
import os
import pickle
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]

def get_authenticated_service(name):
    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "Byte Comic.json"
    credentials_file = f"Files/{name}.pickle"

    # Create OAuth2 authorization flow with a new state parameter
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes, state="")

    # Check if credentials file exists
    if os.path.exists(credentials_file):
        # If credentials file exists, load credentials from it
        with open(credentials_file, 'rb') as token:
            credentials = pickle.load(token)
    else:
        # If credentials file does not exist, perform authorization flow
        credentials = flow.run_local_server()

        # Save credentials to file
        with open(credentials_file, 'wb') as token:
            pickle.dump(credentials, token)

    # Create an API client with the obtained credentials
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

    return youtube


def comm(comment,id,video):
    channel = "UCfjQOWJqoQ69BUaUZtFtGZg"#UC_VigzqI36ljPgtSEdDBETw
    video = video
    commenttext = comment

    # Get authenticated service
    youtube = get_authenticated_service(id)

    request = youtube.commentThreads().insert(
        part="snippet",
        body={
            "snippet": {
                "channelId": channel,
                "videoId": video,
                "topLevelComment": {
                    "snippet":{
                        "textOriginal": commenttext
                        }
                    }
                }
            }
    )
    response = request.execute()

    print(response)
