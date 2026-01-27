from faker import Faker

fake = Faker()

def create_file(num):
    with open(f"datefile{num}.txt", "w") as f:
        for _ in range(100):
            f.write(fake.date() + "\n")

create_file(1)
create_file(2)
