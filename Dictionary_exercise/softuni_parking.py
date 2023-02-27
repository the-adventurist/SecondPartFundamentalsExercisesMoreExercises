parking = {}
n = int(input())

for _ in range(n):
    drivers_data = input().split()
    action = drivers_data[0]
    driver = drivers_data[1]
    if action == 'register':
        license_plate = drivers_data[2]
        if driver not in parking:
            parking[driver] = license_plate
            print(f"{driver} registered {license_plate} successfully")
        else:
            print(f"ERROR: already registered with plate number {license_plate}")
    else:
        if driver not in parking:
            print(f"ERROR: user {driver} not found")
        else:
            del parking[driver]
            print(f"{driver} unregistered successfully")

for name, license_plate in parking.items():
    print(f"{name} => {license_plate}")
