def transform(legacy_data):
	my_list_dict = []
	for key, value in legacy_data.items():
		my_list_dict.extend((i.lower(), key) for i in value)
	return dict(my_list_dict)
