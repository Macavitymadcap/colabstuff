import pandas as pd

xp_thresholds = {
    "easy": [25, 50, 75, 125, 250, 300, 350, 450, 550, 600, 800, 1000, 1100, 1250, 1400, 1600, 2000, 2100, 2400, 2800],
    "medium": [50, 100, 150, 250, 500, 600, 750, 900, 1100, 1200, 1600, 2000, 2200, 2500, 2800, 3200, 3900, 4200, 4900, 5700],
    "hard": [75, 150, 225, 375, 750, 900, 1100, 1400, 1600, 1900, 2400, 3000, 3400, 3800, 4300, 4800, 5900, 6300, 7300, 8500],
    "deadly": [100, 200, 400, 500, 1100, 1400, 1700, 2100, 2400, 2800, 3600, 4500, 5100, 5700, 6400, 7200, 8800, 9500, 10900, 12700]
}
xp_df = pd.DataFrame(xp_thresholds, index=[num + 1 for num in range(20)])
xp_df.index.name = "Level"

xp_by_cr = {
    "XP": [10, 25, 50, 100, 200, 450, 700, 1100, 1800, 2300, 2900, 3900, 5000, 5900, 7200, 8400, 10000, 11500, 13000, 15000, 18000, 20000, 22000, 25000, 33000, 41000, 50000, 62000, 75000, 90000, 105000, 120000, 135000, 155000]
}
xp_cr_df = pd.DataFrame(xp_by_cr, index=["0", "1/8", "1/4", "1/2", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30"])
xp_cr_df.index.name = "CR"

mult_fewer_three = {
    "multiplier": [1.5, 2, 2.5, 2.5, 2.5, 2.5, 3, 3, 3, 3, 4, 4, 4, 4, 5]
}
fewer_three_df = pd.DataFrame(mult_fewer_three, index=[num + 1 for num in range(15)])
fewer_three_df.index.name = "num monsters"

mult_three_five = {
    "multiplier": [1, 1.5, 2, 2, 2, 2, 2.5, 2.5, 2.5, 2.5, 3, 3, 3, 3, 4]
}
three_five_df = pd.DataFrame(mult_three_five, index=[num + 1 for num in range(15)])
three_five_df.index.name = "num monsters"

mult_six_plus = {
    "multiplier": [0.5, 1, 1.5, 1.5, 1.5, 1.5, 2, 2, 2, 2, 2.5, 2.5, 2.5, 2.5, 3]
}
six_plus_df = pd.DataFrame(mult_six_plus, index=[num + 1 for num in range(15)])
six_plus_df.index.name = "num monsters"

def calculate_difficulty():
  num_pcs = input("How many PCs? ")
  pcs = int(num_pcs)
  levels = []
  for num in range(pcs):
    pc_level = input(f"  Player {num+1}'s level? ")
    level = int(pc_level)
    levels.append(level)
  easy, medium, hard, deadly = 0, 0, 0, 0
  for i in levels:
    easy += xp_df.at[i, "easy"]
    medium += xp_df.at[i, "medium"]
    hard += xp_df.at[i, "hard"]
    deadly += xp_df.at[i, "deadly"]
  print("")
  num_monsters = input("How many monsters? ")
  monsters = int(num_monsters)
  total_xp, modified_xp = 0, 0
  for num in range(monsters):
    monster_cr = input(f"  Monster {num+1}'s CR? ")
    xp = int(xp_cr_df.at[monster_cr, "XP"])
    total_xp += xp
  if monsters <= 15:
    if pcs < 3:
      modified_xp = total_xp * fewer_three_df.at[monsters, "multiplier"]
    elif pcs >= 3 and pcs <= 5:
      modified_xp = total_xp * three_five_df.at[monsters, "multiplier"]
    else:
      modified_xp = total_xp * six_plus_df.at[monsters, "multiplier"]
  else:
    if pcs < 3:
      modified_xp = total_xp * fewer_three_df.at[15, "multiplier"]
    elif pcs >= 3 and pcs > 5:
      modified_xp = total_xp * three_five_df.at[15, "multiplier"]
    else:
      modified_xp = total_xp * six_plus_df.at[15, "multiplier"]
  mod_xp = int(modified_xp)
  print("")
  if mod_xp < medium:
    print(f"Encounter Difficulty: Easy\n  Total XP: {total_xp}\n  Modifed XP: {mod_xp}\n  XP per Player: {int(total_xp / pcs)}")
  elif mod_xp >= medium and mod_xp < hard:
    print(f"Encounter Difficulty: Medium\n  Total XP: {total_xp}\n  Modifed XP: {mod_xp}\n  XP per Player: {int(total_xp / pcs)}")
  elif mod_xp >= hard and mod_xp < deadly:
    print(f"Encounter Difficulty: Hard\n  Total XP: {total_xp}\n  Modifed XP: {mod_xp}\n  XP per Player: {int(total_xp / pcs)}")
  elif mod_xp >= deadly:
    print(f"Encounter Difficulty: Deadly\n  Total XP: {total_xp}\n  Modifed XP: {mod_xp}\n  XP per Player: {int(total_xp / pcs)}")
  print("")
  yesno = ["yes", "no"]
  res = ""
  while res not in yesno:
    res = input("Calculate another encounter? ").lower()
    if res == "yes":
      print("")
      calculate_difficulty()
    elif res == "no":
      return
    else:
      print("Type 'yes' or 'no'.")

calculate_difficulty()
