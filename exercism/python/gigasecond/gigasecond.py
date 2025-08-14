from datetime import timedelta
def add(moment):
	giga_seconds = 1_000_000_000

	future_time = moment + timedelta(seconds=giga_seconds)

	return future_time
