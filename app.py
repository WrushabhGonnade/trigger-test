import requests
import requests
import json
import git

project_name = 'Hello World'
api_key="API-FURAOUECZ3M6VELG044KJRRZB9VFYPB"

headers = {
    'X-Octopus-ApiKey': api_key,
    'Content-Type': 'application/json'
}
octopus_cloud_url="https://wrushu.octopus.app"
response = requests.get(octopus_cloud_url, headers=headers)
print(response.status_code)

response = requests.get(octopus_cloud_url + '/api/projects/all', headers=headers)
response.raise_for_status()
projects = response.json()

project_id = next((project['Id'] for project in projects if project['Name'] == project_name), None)
print("Project Id: ",project_id)
if not project_id:
    raise ValueError(f"No project found with name '{project_name}'.")

repo = git.Repo('.')
latest_commit_message = repo.head.commit.message
print(latest_commit_message)

project_id=project_id
version="2020.1.10"
release_note=latest_commit_message

data = {
    'ProjectId': project_id,
    'Version': version,
    'ReleaseNotes': release_note
}

response = requests.post(octopus_cloud_url+'/api/releases', headers=headers, data=json.dumps(data))

if response.status_code == 201:
    print('Release created successfully with the latest commit message!')
else:
    print('Error creating release. Status code: ' + str(response.status_code))










