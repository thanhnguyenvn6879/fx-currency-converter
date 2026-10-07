def format_result(date, from_currency, to_currency, rate, from_amount):
    to_amount = rate * from_amount
    inverse_rate = 1 / rate
    return (f"The conversion rate on {date} from {from_currency} to {to_currency} was {rate}. "
            f"So {from_amount} in {from_currency} corresponds to {to_amount} in {to_currency}. "
            f"The inverse rate was {inverse_rate:.4f}.")
