from psnawp_api import PSNAWP
from psnawp_api.models import SearchDomain
from psnawp_api.models.trophies import PlatformType

psnawp = PSNAWP("seucodigonpssoaqui")

# Your Personal Account Info
client = psnawp.me()
print(f"Online ID: {client.online_id}")
print(f"Account ID: {client.account_id}")
print(f"Profile: {client.get_profile_legacy()} \n")

# Your Registered Devices
devices = client.get_account_devices()
for device in devices:
    print(f"Device: {device} \n")

# Your Friends List
friends_list = client.friends_list()
for friend in friends_list:
    print(f"Friend: {friend} \n")

# Your Players Blocked List
blocked_list = client.blocked_list()
for blocked_user in blocked_list:
    print(f"Blocked User: {blocked_user} \n")

# Your Friends in "Notify when available" List
available_to_play = client.available_to_play()
for user in available_to_play:
    print(f"Available to Play: {user} \n")

# Your trophies (PS4)
for trophy in client.trophies("NPWR25000_00", PlatformType.PS4):
    print(trophy)

# Your Chat Groups
groups = client.get_groups()
first_group_id = None  # This will be used later to test group methods
if groups:  # Verifica se há grupos disponíveis
    for id, group in enumerate(groups):
        if id == 0:  # Get the first group ID
            first_group_id = group.group_id

        group_info = group.get_group_information()
        print(f"Group {id}: {group_info} \n")
else:
    print("No groups found.")

# Your Playing time (PS4, PS5 above only)
titles_with_stats = client.title_stats()
for title in titles_with_stats:
    print(
        f" \
        Game: {title.name} - \
        Play Count: {title.play_count} - \
        Play Duration: {title.play_duration} \n"
    )

# Other User's
example_user_1 = psnawp.user(online_id="VaultTec-Co")  # Get a PSN player by their Online ID
print(f"User 1 Online ID: {example_user_1.online_id}")
print(f"User 1 Account ID: {example_user_1.account_id}")

print(example_user_1.profile())
print(example_user_1.prev_online_id)
print(example_user_1.get_presence())
print(example_user_1.friendship())
print(example_user_1.is_blocked())

# Example of getting a user by their account ID
user_account_id = psnawp.user(account_id="9122947611907501295")
print(f"User Account ID: {user_account_id.online_id}")

# Messaging and Groups Interaction
group = psnawp.group(group_id=first_group_id)  # This is the first group ID we got earlier - i.e. the first group in your groups list
print(group.get_group_information())
print(group.get_conversation(10))  # Get the last 10 messages in the group
print(group.send_message("Hello World"))
# print(group.change_name("API Testing 3"))
# print(group.leave_group()) # Uncomment to leave the group

# Create a new group with other users - i.e. 'VaultTec-Co' and 'test'
example_user_2 = psnawp.user(online_id="test")
new_group = psnawp.group(users_list=[example_user_1, example_user_2])
print(new_group.get_group_information())
# You can use the same above methods to interact with the new group - i.e. send messages, change name, etc.

# Searching for Game Titles
search = psnawp.search(search_query="GTA 5", search_domain=SearchDomain.FULL_GAMES)
for search_result in search:
    print(search_result["result"]["invariantName"])
