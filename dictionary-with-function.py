def run():
    print('VROOM')

corvette = {
    "color": "Red",
    "run": run
}

print("My", corvette["color"],"can go")
corvette["run"]()

myrun = corvette["run"]
myrun()