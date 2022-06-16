my_list = open("my-anime-list.txt", mode="w")

my_list.write("Sword Art Online\n")
my_list.write("Full Metal Alchimist\n")
my_list.write("Konosuba\n")
my_list.write("Spy Vs Family\n")

print("Doctor Stone", file=my_list)
print("Evangelion", file=my_list)
print("Shingeki No Kyojin", file=my_list)
print("Overlord", file=my_list)

more_animes = [
    "Kimetsu No Yaba\n",
    "Shingatsu Wa Kimi No Uso\n",
    "Your Name\n",
    "Ishuzoku Revierws"]

my_list.writelines(more_animes)

my_list.close()
