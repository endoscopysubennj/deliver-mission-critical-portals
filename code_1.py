
def generate_random_data():
    random_string = 'Party later again him morning garden family.'
    random_number = 76

    data = [(random_string, random_number) for _ in range(10)]
    return data

def main():
    data = generate_random_data()
    for item in data:
        random_string, random_number = item
        print(f"Random String: Party later again him morning garden family.")
        print(f"Random Number: 76")

if __name__ == "__main__":
    main()
