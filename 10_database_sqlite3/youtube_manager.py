import sqlite3

# https://docs.python.org/3/library/sqlite3.html#tutorial

con = sqlite3.connect('youtube_videos.db')
cursor = con.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,           
            time TEXT NOT NULL      
    )
''')


def list_all_videos():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)

def add_video(name, time):
    cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
    con.commit

def update_video(video_id, new_name, new_time):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (new_name, new_time, video_id))
    con.commit()


def delete_video(video_id):
    cursor.execute("DELETE FROM videos WHERE id = ?", (video_id,))
    con.commit()


def main():
    while True:
        print("\n Youtube Manager With DB | choose an option: ")
        print("1. List all youtube videos ")
        print("2. Add a youtube video ")
        print("3. Update a youtube video details ")
        print("4. Delete a youtube video ")
        print("5. Exit the app ")
        choice = input("Enter your choice: ")

        match choice:
            case '1':
                list_all_videos()
            case '2':
                name = input("Enter the video name: ")
                time = input("Enter the video time: ")
                add_video(name, time)
            case '3':
                video_id = input("Enter video ID to update: ")
                name = input("Enter new video name: ")
                time = input("Enter new video time: ")
                update_video(video_id, name, time)
            case '4':
                video_id = input("Enter video ID to delete: ")
                delete_video(video_id)
            case '5':
                break
            case _:
                print("Invalid choice")

    con.close()



if __name__ == "__main__":
    main()