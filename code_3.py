
def generate_random_data():
    random_string = 'Thing despite rate.'
    random_number = 1

    data = [(random_string, random_number) for _ in range(10)]
    return data

def main():
    data = generate_random_data()
    for item in data:
        random_string, random_number = item
        print(f"Random String: Thing despite rate.")
        print(f"Random Number: 1")

if __name__ == "__main__":
    main()
