def transform(legacy_data):
	return {
			i.lower(): key
			for key, value in legacy_data.items()
			for i in value
		}
