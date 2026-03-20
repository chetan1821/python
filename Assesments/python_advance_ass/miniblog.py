import os

class User:
    def __init__(self, name):
        self.name = name

class Post:
    def __init__(self, user, title, content):
        self.user = user
        self.title = title
        self.content = content

    def save_to_file(self):
        try:
            # Create filename
            filename = f"{self.user.name}_{self.title}.txt"

            # Replace spaces with underscore
            filename = filename.replace(" ", "_")

            with open(filename, "w") as file:
                file.write(f"Author: {self.user.name}\n")
                file.write(f"Title: {self.title}\n\n")
                file.write(self.content)

            print("Post saved successfully!")

        except Exception as e:
            print("Error saving file:", e)


# -------------------------------
# Create Post Function
# -------------------------------
def create_post():
    try:
        name = input("Enter your name: ").strip()
        title = input("Enter post title: ").strip()
        content = input("Enter post content: ").strip()

        if not name or not title or not content:
            raise ValueError("All fields are required!")

        user = User(name)
        post = Post(user, title, content)

        post.save_to_file()

    except ValueError as ve:
        print("⚠️", ve)


# -------------------------------
# View Posts Function
# -------------------------------
def view_posts():
    try:
        files = [f for f in os.listdir() if f.endswith(".txt")]

        if not files:
            print("⚠️ No posts found!")
            return

        print("\n📂 Available Posts:")
        for i, file in enumerate(files, start=1):
            print(f"{i}. {file}")

        choice = int(input("Select file number: "))

        if choice < 1 or choice > len(files):
            raise IndexError("Invalid choice!")

        filename = files[choice - 1]

        with open(filename, "r") as file:
            print("\n📖 Post Content:\n")
            print(file.read())

    except FileNotFoundError:
        print("❌ File not found!")
    except ValueError:
        print("❌ Please enter a valid number!")
    except IndexError as ie:
        print("❌", ie)


# -------------------------------
# Main Menu
# -------------------------------
def main():
    while True:
        print("\n====== MiniBlog ======")
        print("1. Create Post")
        print("2. View Posts")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_post()
        elif choice == "2":
            view_posts()
        elif choice == "3":
            print("👋 Exiting MiniBlog...")
            break
        else:
            print("❌ Invalid choice! Try again.")


# Run App
main()