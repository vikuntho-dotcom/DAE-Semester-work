
# Python 1 Project: Sports Search

# List of available sports
sport_options = ["Soccer", "Football", "Baseball", "Ice Hockey"]


# Function that displays all available sports
def display_sports():
    print("\nThe options you have are:")

    # Loop through the sports list
    for index, sport_name in enumerate(sport_options):
        print(f"{index + 1}. {sport_name}")


# Function that finds the location of the selected sport
def find_location(selected_sport):

    if selected_sport == "1":
        return "Los Angeles"

    elif selected_sport == "2":
        return "Gillette Stadium"

    elif selected_sport == "3":
        return "Fenway Park"

    elif selected_sport == "4":
        return "TD Garden"

    else:
        return "Out of options!"


# String variable
search_again = "yes"

# Integer variable
search_count = 0

print("Welcome to Sports Search!")


# Loop that allows users to search multiple times
while search_again == "yes":

    # Display the available sports
    display_sports()

    # Ask the user to select a sport
    selected_sport = input(
        "\nSelect a sport from the options (1-4): "
    )

    # Boolean variable to check the selection
    valid_selection = selected_sport in ["1", "2", "3", "4"]

    # Decision-making structure
    if valid_selection:

        # Find and display the sports location
        location = find_location(selected_sport)

        print("\nYour location is:", location)

        # Add one to the successful search count
        search_count += 1

    else:
        print("\nOut of options! Please select 1-4.")

    # Ask if the user wants to search again
    search_again = input(
        "\nDo you want to search again? (yes/no): "
    ).strip().lower()


# Display the final message
print("\nThanks for using Sports Search!")

# Display total successful searches
print("Total successful searches:", search_count)
