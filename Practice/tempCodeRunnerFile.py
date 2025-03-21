import matplotlib.pyplot as plt
data_Irfan = {
    "skill": ["javaScript", "python", "github", "c++"],
    "semister": ["1st", "2nd", "3rd", "4th"],
}
data_mahin = {
    "skill": ["javaScript", "python","", "c++"],
    "semister": ["1st", "2nd", "3rd", "4th"],
}

plt.plot( data_Irfan["semister"], data_Irfan["skill"], label="Irfan the Boss", color="red", linestyle="-")
plt.plot(data_mahin["semister"],data_mahin["skill"],  label="Mahin the mao", color="blue", linestyle="--")

plt.legend()
plt.xlabel("semister")
plt.ylabel("skill")
plt.title("Growth of mentality")
plt.show()