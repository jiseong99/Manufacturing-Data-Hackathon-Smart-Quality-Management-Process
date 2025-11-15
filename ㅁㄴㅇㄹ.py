import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("qlearning.csv", sep=";")

for env in ["cafeWorld", "bookWorld"]:
    sub = df[df["Env"] == env]
    plt.figure()
    plt.plot(sub["Episode #"], sub["Cumulative Reward"])
    plt.xlabel("Episode")
    plt.ylabel("Cumulative Reward")
    plt.title(env)
    plt.savefig(f"qlearning_{env}.png")
