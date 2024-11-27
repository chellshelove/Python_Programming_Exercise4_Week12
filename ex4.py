from collections import Counter

# Open the file in read mode
with open("songs.txt", "r") as file:
    singers = []  # List to store singers
    
    # Read each line in the file
    for line in file:
        parts = line.strip().split()  # Split the line into parts
        if len(parts) > 2:  # Ensure the line has at least a singer, title, and count
            singer = parts[0][1:]  # Remove the leading "-" from the singer
            singers.append(singer.strip())  # Add the singer to the list

# Count the occurrences of each singer
singer_counts = Counter(singers)

# Find the singer with the most songs
most_songs_singer = max(singer_counts, key=singer_counts.get)
most_songs_count = singer_counts[most_songs_singer]

# Print the result
print(f"Singer with the most songs: {most_songs_singer}")
print(f"Number of songs: {most_songs_count}")