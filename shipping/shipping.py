
def cost_gs(weight):
  cost = 0
  if weight <= 2:
    cost = (1.5 * weight) + 20
  elif weight > 2 and weight <= 6:
    cost = (3 * weight) + 20
  elif weight > 6 and weight <= 10:
    cost = (4 * weight) + 20
  else:
    cost = (4.75 * weight) + 20
  return cost

print(cost_gs(8.4))

premium_gs = 125

def cost_ds(weight):
  cost = 0
  if weight <= 2:
    cost = (4.5 * weight)
  elif weight > 2 and weight <= 6:
    cost = (9 * weight)
  elif weight > 6 and weight <= 10:
    cost = (12 * weight)
  else:
    cost = (14.25 * weight)
  return cost

print(cost_ds(1.5))

def cheapest(weight):
  cost = 0
  if int(cost_gs(weight)) < premium_gs and int(cost_gs(weight)) < int(cost_ds(weight)):
    return "The cheapest method of shipping is Ground Shipping. Cost of this shipping is " + str(cost_gs(weight)) + " $ ." 
  elif int(cost_ds(weight)) < premium_gs and int(cost_ds(weight)) < int(cost_gs(weight)):
    return "The cheapest method of shipping is Drone Shipping. Cost of this shipping is " + str(cost_ds(weight)) + " $ ." 
  else:
    return "The cheapest method of shipping is Premium Ground Shipping.Cost of this shipping is " + str(premium_gs) + " $ ."

print(cheapest(4.8))
print (cheapest(41.5))