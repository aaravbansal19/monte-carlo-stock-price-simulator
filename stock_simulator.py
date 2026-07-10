# Imports random library 
import random
import matplotlib.pyplot as plt
import statistics
 
 # Defines main variables 
starting_price = 100
simulations = 10000
days = 252

# This function runs the entire simulations and saves all the simulation ending price in the list, final_prices. 
def run_simulation():

    # Sets all variables 
    current_price = starting_price
    final_prices = []

    # Prints starting variable info and introduction. 
    print()
    print("Monte Carlo Stock Price Simulation")
    print()
    print(f"Starting Price: ${starting_price:.2f}")
    print(f"Trading Days: {days}")
    print(f"Simulations: {simulations}")
    print()

    # Prints the final price for an amount of simulations. 
    for simulation in range(simulations):
        # Prints each day price in a simulation. 
        for day in range(1, days + 1):
            # Simulates a daily stock return using a normal distribution
            # Mean daily return = 0.03%
            # Daily volatility = 1%
            daily_return = random.gauss(0.0003, 0.01)
            # Saves random price 
            current_price = current_price * (1 + daily_return)
        # Adds each simulation end price to list, and rounds the final price to 2 decimal points.  
        final_prices.append(round(current_price, 2))
        # Resets each simulation to the starting price. 
        current_price = starting_price

    # Prints ending message 
    print(f"Completed all {simulations} simulations. ")
    print()

    # Returns the final_prices list
    return final_prices

# This function calculates all the statistical measures and saves them in variables to be printed in a report later. 
def calculate_statistics(final_prices, starting_price):
    # Calculates the average final price
    avg = sum(final_prices) / len(final_prices) if final_prices else 0    
    avg = round(avg, 2)

    # Calculates the highest and lowest final price, with ensuring if the final_prices list is empty, the variables will be zero. 
    highest = max(final_prices) if final_prices else 0
    lowest = min(final_prices) if final_prices else 0

    # Calculates the median and standard deviation using the statistics library. 
    if len(final_prices) > 1:
        std = statistics.stdev(final_prices) 
    else:
        std = 0
    median = statistics.median(final_prices) if final_prices else 0
    # Counts simulations above and below the starting price. 
    above_starting = 0
    below_starting = 0
    # Iterates through list to check
    for price in final_prices:
        if price > starting_price:
            above_starting += 1
        elif price < starting_price:
            below_starting += 1

    return avg, median, highest, lowest, std, above_starting, below_starting

# This function calculates all the percent chances of different scenarios and different measurements, saving them in variables to be printed later. 
def calculate_probabilities(final_prices, starting_price, simulations):
    # Defines the profit and loss variables. 
    profitable = 0
    losses = 0
    same = 0

    gain_10 = 0
    gain_20 = 0

    loss_10 = 0
    loss_20 = 0

    # Increments the variables for how many simulations match each variable. 
    for price in final_prices:
        if price > starting_price:
            profitable += 1
        elif price < starting_price:
            losses += 1 
        else:
            same += 1
        if price >= starting_price * 1.10:
            gain_10 += 1
        if price >= starting_price * 1.20:
            gain_20 += 1
        if price <= starting_price * 0.90:
            loss_10 += 1
        if price <= starting_price * 0.80:
            loss_20 += 1

    # Calculates the percent chance of each variable occurring. 
    profit_probability = profitable / simulations * 100
    loss_probability = losses / simulations * 100
    same_probability = same / simulations * 100
    gain10_probability = gain_10 / simulations * 100
    gain20_probability = gain_20 / simulations * 100
    loss10_probability = loss_10 / simulations * 100
    loss20_probability = loss_20 / simulations * 100

    return (
    profit_probability,
    loss_probability,
    same_probability,
    gain10_probability,
    gain20_probability,
    loss10_probability,
    loss20_probability
    )

# This function prints the full report and summary. 
def print_summary(
    avg,
    median,
    highest,
    lowest,
    std,
    above_starting,
    below_starting,
    profit_probability,
    loss_probability,
    same_probability,
    gain10_probability,
    gain20_probability,
    loss10_probability,
    loss20_probability
    ):  
    # Prints the statistical report
    print("Simulation Summary: ")
    print()
    # Prints average, highest, and lowest final price. 
    print(f"Average Final Price: ${avg:.2f}")
    print(f"Median Final Price: ${median:.2f}")
    print(f"Highest Final Price: ${highest:.2f}")
    print(f"Lowest Final Price: ${lowest:.2f}")
    print(f"Standard Deviation: ${std:.2f}")
    print()
    # Prints how much simulations are above and below $100. 
    print(f"Simulations ending above $100: {above_starting}")
    print(f"Simulations ending below $100: {below_starting}")
    print()
    # Prints the profit and loss probabilities. 
    print(f"Chance of Profit: {profit_probability:.2f}%")
    print(f"Chance of Loss: {loss_probability:.2f}%")
    print(f"Chance of staying at starting price: {same_probability:.2f}%")
    print()
    print(f"Chance of gaining at least 10%: {gain10_probability:.2f}%")
    print(f"Chance of gaining at least 20%: {gain20_probability:.2f}%")
    print()
    print(f"Chance of losing at least 10%: {loss10_probability:.2f}%")
    print(f"Chance of losing at least 20%: {loss20_probability:.2f}%")
    print()

# This functions graphs a histogram to show the data. 
def plot_histogram(final_prices, starting_price, avg):
    # Creates a histogram representing the data
    plt.figure(figsize=(10,6))
    plt.hist(final_prices, bins=50, edgecolor="black", alpha = 0.75)
    plt.title("Monte Carlo Simulation Final Prices")
    plt.xlabel("Final Stock Price ($)")
    plt.ylabel("Frequency")
    plt.grid(alpha=0.3)
    plt.axvline(starting_price, color="red", linestyle="--", linewidth=2, label = "Starting Price")
    plt.axvline(avg, color="green", linestyle="-", linewidth=2, label = f"Average = ${avg:.2f}")
    plt.legend()
    plt.tight_layout()
    plt.savefig("simulation_histogram.png")
    plt.show()
    plt.close()

# This function calls all the other functions
def main():
    final_prices = run_simulation()

    avg, median, highest, lowest, std, above_starting, below_starting = calculate_statistics(final_prices, starting_price)    
    profit_probability, loss_probability, same_probability, gain10_probability, gain20_probability, loss10_probability, loss20_probability = calculate_probabilities(final_prices,starting_price, len(final_prices))
    print_summary(avg,
        median, highest, lowest, std, above_starting, below_starting, profit_probability, loss_probability, same_probability, gain10_probability, gain20_probability, loss10_probability, loss20_probability)
    plot_histogram(final_prices, starting_price, avg)

# Runs the main() function only when the file is executed directly, not when it is imported. 
if __name__ == "__main__":
    main()