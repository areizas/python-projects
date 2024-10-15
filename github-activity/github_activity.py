import requests
import sys

def get_latest_events(username):
  url = f"https://api.github.com/users/{username}/events"
  try:
    response = requests.get(url)
    if (response.status_code == 200):
      data = response.json()
      for event in data:
        match event['type']:
          case 'PullRequestReviewCommentEvent':
            print(f"- Commented on PR {event['payload']['pull_request']['html_url']}")
          case 'PullRequestReviewEvent':
            print(f"- Reviewed on PR {event['payload']['pull_request']['html_url']}")
          case 'PushEvent':
            print(f"- Pushed a commit in repo {event['repo']['name']}")
          case 'PullRequestEvent':
            print(f"- Created a PR in repo {event['repo']['name']}")
          case _:
            print(f"- {event['type']} in {event['repo']['name']}")

    else:
      print(f"The username {username} has not been found as an active github user.") 
  except:
    print(f"There was an error with the request")


if __name__ == "__main__":

  if len(sys.argv) > 1:
    get_latest_events(sys.argv[1])
  else:
    print("An user name must be provided.")
  