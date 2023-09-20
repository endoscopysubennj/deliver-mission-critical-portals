
def generate_random_data():
    random_string = 'Quite follow dinner.'
    random_number = 94

    data = [(random_string, random_number) for _ in range(10)]
    return data

def main():
    data = generate_random_data()
    for item in data:
        random_string, random_number = item
        print(f"Random String: Quite follow dinner.")
        print(f"Random Number: 94")

if __name__ == "__main__":
    main()
