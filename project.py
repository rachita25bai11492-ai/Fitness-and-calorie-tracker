consumed = []
burned = []

for i in range(1, 8):
    consumed.append(int(input(f"Day {i} consumed: ")))
    burned.append(int(input(f"Day {i} burned: ")))

balance = [consumed[i] - burned[i] for i in range(7)]
total_balance = sum(balance)

print("\nTotal Consumed:", sum(consumed))
print("Total Burned:", sum(burned))
print("Daily Balance:", balance)
print("Weekly Balance:", total_balance)

if total_balance > 0:
    print("Recommendation: Calorie SURPLUS – reduce intake or exercise more.")
elif total_balance < 0:
    print("Recommendation: Calorie DEFICIT – eat a bit more.")
else:
    print("Recommendation: Perfect balance!")