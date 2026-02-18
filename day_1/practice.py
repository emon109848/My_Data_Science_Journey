def remove_duplicates(lst):
	"""Return a new list with duplicates removed while preserving order.

	Example:
	>>> remove_duplicates([1,2,2,3,1])
	[1, 2, 3]
	"""
	seen = set()
	result = []
	for item in lst:
		if item not in seen:
			result.append(item)
			seen.add(item)
	return result


if __name__ == "__main__":
	examples = [
		[1, 2, 2, 3, 4, 1],
		["a", "b", "a", "c", "b"],
		[1, "1", 1, "1"],
	]

	for ex in examples:
		print("Original:", ex)
		print("Without duplicates:", remove_duplicates(ex))
		print()

