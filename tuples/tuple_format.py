def guest_list(guests):
 for guest in guests:
  a, b, c = guest
  greet = "{} is {} years old and works as {}."
  print(greet.format(a, b, c))


guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])