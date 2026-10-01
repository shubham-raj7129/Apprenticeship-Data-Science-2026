import re


DATA = (
	"In the upcoming year, several prominent stocks are predicted to reach significant highs, "
	"reflecting the market's dynamic nature and investor confidence in these companies. Apple "
	"Inc. (AAPL) is expected to reach around $198, showcasing its continued dominance in the "
	"tech industry. Amazon.com Inc. (AMZN) is predicted to soar to approximately $3,773, "
	"driven by a surge in online retail demand. Microsoft Corporation (MSFT) could reach "
	"around $367 as it solidifies its position in cloud computing. Similarly, Tesla Inc. "
	"(TSLA) is anticipated to see its stock price climb to about $415, fueled by its "
	"leadership in electric vehicles. Alphabet Inc. (GOOGL) may hit around $152, reflecting "
	"its robust digital advertising revenue. In the semiconductor industry, NVIDIA Corporation "
	"(NVDA) is forecasted to peak at approximately $503, driven by advancements in AI and "
	"gaming technology. Meta Platforms Inc. (META) is expected to achieve a high of around "
	"$382, amid a surge in social media engagement and advertising. Berkshire Hathaway Inc. "
	"(BRK.A), known for its diversified investments, could see its shares reach a staggering "
	"$570,000. Johnson & Johnson (JNJ), a leader in pharmaceuticals and consumer health "
	"products, might hit around $187. The Coca-Cola Company (KO), with its strong global "
	"brand, is anticipated to reach about $65, highlighting its resilience. Procter & Gamble "
	"Co. (PG), a household name in consumer goods, is expected to achieve a high of "
	"approximately $165. Finally, The Walt Disney Company (DIS) may reach around $203, "
	"reflecting its successful expansion into streaming and media content. These potential "
	"highs underscore the diverse strengths and market positions of these leading companies."
)


def extract_stock_data(paragraph):
	"""Extract stock symbols and predicted values from freeform paragraph text."""
	names = []
	values = {}

	symbol_pattern = re.compile(r"\(([A-Z]+(?:\.[A-Z]+)?)\)")

	for match in symbol_pattern.finditer(paragraph):
		symbol = match.group(1)

		# Check nearby text after the symbol for the first dollar amount.
		window = paragraph[match.end() : match.end() + 120]
		price_match = re.search(r"\$([0-9][0-9,]*(?:\.[0-9]+)?)", window)

		if price_match:
			price_text = price_match.group(1)
			values[symbol] = int(price_text.replace(",", ""))
			names.append(symbol)

	return names, values


def display_menu():
	print("\nEnter the number of the corresponding action you desire.\n")
	print("1. Print a list of stock symbols included in the list.")
	print("2. Retrieve the estimated 12 month high for a stock.")
	print("3. Exit")


def main():
	names, stock_values = extract_stock_data(DATA)

	print("Your stock list is now available.")

	while True:
		display_menu()
		try:
			choice = input("ACTION:> ").strip()
		except (KeyboardInterrupt, EOFError):
			print("\nGoodbye.")
			break

		if choice == "1":
			for symbol in sorted(names):
				print(symbol)

		elif choice == "2":
			user_symbol = input("Enter the stock symbol:> ").strip().upper()

			if user_symbol in stock_values:
				print(
					f"\nThe estimated 12 month peak for {user_symbol} "
					f"is ${stock_values[user_symbol]:,}."
				)
			else:
				print("Invalid stock symbol. Please try again.")

		elif choice == "3":
			print("Goodbye.")
			break

		else:
			print("Invalid action. Please enter 1, 2, or 3.")


if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		print("\nGoodbye.")
