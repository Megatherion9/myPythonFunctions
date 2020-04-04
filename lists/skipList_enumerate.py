def skip_elements(elements):

  skipped_elements = []
  for index, content in enumerate(elements):
    if index % 2 == 0:
      skipped_elements.append(content)

  return skipped_elements

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']

