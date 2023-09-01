def main():
    with open("file_to_read.txt", "r") as file:
        input_text = file.read()

    terrible_count = input_text.lower().count("terrible")

    new_text = input_text.replace("terrible", "pathetic", terrible_count % 2 == 0)
    new_text = new_text.replace("terrible", "marvellous")

    with open("result.txt", "w") as f:
        f.write(f"New text:\n{new_text}\n")
        f.write(f"terrible appear: {terrible_count} times")

    print("mission complete")


if __name__ == "__main__":
    main()
