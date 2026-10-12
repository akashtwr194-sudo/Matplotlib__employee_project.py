import pandas as pd
import matplotlib.pyplot as plt
 
#==============================
#1. Load Data
#==============================
df = pd.read_csv("employees.csv") 
print(df.head())
print(df.columns)
 
#==============================
#2. Reports
#==============================
 
# Team Wise Total Salary
team_salary = df.groupby("Team")["Salary"].sum()
team_salary = team_salary.sort_values(ascending=False)
 
#Gender Wise Employees
gender_report = df["Gender"].value_counts()
 
# Team Wise Employee Count
employee_count = df["Team"].value_counts()

# Team Wise Average Salary
average_salary = df.groupby("Team")["Salary"].mean()
average_salary = average_salary.sort_values(ascending=False)
# 
# ==============================
# 3. Dashboard
#==============================
 
fig, ax = plt.subplots(2, 2, figsize=(15, 10))
 
#==============================
#1. Team Wise Salary
#==============================
ax[0,0].bar(team_salary.index,team_salary.values,color="steelblue")
 
ax[0,0].set_title("Team Wise Total Salary")
ax[0,0].set_xlabel("Team")
ax[0,0].set_ylabel("Total Salary")
ax[0,0].tick_params(axis="x", rotation=45)
ax[0,0].grid(axis="y")
 
#==============================
# 2. Gender Distribution
#============================== 
ax[0,1].pie(gender_report.values,labels=gender_report.index,autopct="%1.1f%%",startangle=90)
ax[0,1].set_title("Gender Distribution")
 
# ==============================
# 3. Employee Count
#==============================
 
ax[1,0].bar(employee_count.index,employee_count.values,color="orange")
 
ax[1,0].set_title("Employees Per Team")
ax[1,0].set_xlabel("Team")
ax[1,0].set_ylabel("Number of Employees")
ax[1,0].tick_params(axis="x", rotation=45)
ax[1,0].grid(axis="y")
 
#==============================
# 4. Average Salary
#==============================
 
ax[1,1].barh(average_salary.index,average_salary.values,color="green")
 
ax[1,1].set_title("Average Salary By Team")
ax[1,1].set_xlabel("Average Salary")
ax[1,1].set_ylabel("Team")
ax[1,1].grid(axis="x")
# 
# ==============================
# Dashboard Title
# ==============================
 
fig.suptitle("EMPLOYEE ANALYTICS DASHBOARD",fontsize=18,fontweight="bold",color="black")
 
plt.tight_layout()
 
plt.savefig("Employee_Dashboard.png",dpi=300)
 
plt.show()
 

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("employees.csv")
print(df)
print(df.head())
print(df.columns)

team_salary = df.groupby("Team")["Salary"].sum()
print(team_salary)
gender_report = df["Gender"].value_counts()
print(gender_report)
employee_count = df["Team"].value_counts()
average_salary = df.groupby("Team")["Salary"].mean()

fig, ax = plt.subplots(2, 2, figsize=(18,9 ))

ax[0,0].bar(team_salary.index,team_salary.values,color="steelblue")
ax[0,0].set_title("Team Wise Total Salary")
ax[0,0].set_xlabel("Team")
ax[0,0].set_ylabel("Total Salary")
ax[0,0].tick_params(axis="x", rotation=45)
ax[0,0].grid(axis="y")

ax[0,1].hist(df["Salary"],bins=20,color="Green")

ax[0,1].set_title("Salary Distribution")
ax[0,1].set_xlabel("Salary")
ax[0,1].set_ylabel("Number of Employees")
ax[0,1].grid(axis="y")


ax[1,0].bar(employee_count.index,employee_count.values,color="orange")
ax[1,0].set_title("Employees Per Team")
ax[1,0].set_xlabel("Team")
ax[1,0].set_ylabel("Number of Employees")
ax[1,0].tick_params(axis="x", rotation=50)
ax[1,0].grid(axis="y")

ax[1,1].barh(average_salary.index,average_salary.values,color="green") 
ax[1,1].set_title("Average Salary By Team")
ax[1,1].set_xlabel("Average Salary")
ax[1,1].set_ylabel("Team")
ax[1,1].grid(axis="x")

fig.suptitle("EMPLOYEE ANALYTICS DASHBOARD",fontsize=17,fontweight="bold",color="black")
plt.tight_layout()
plt.savefig("Employee_Dashboard.png",dpi=300)
plt.show()


import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("employees.csv")
print(df)

management_report = df["Senior Management"].value_counts()
print(management_report)
plt.figure(figsize=(8,5))
plt.bar(management_report.index,management_report.values,color="orange")

plt.title("Senior Management")
plt.xlabel("Senior Management")
plt.ylabel("Number of Employees")
plt.suptitle("SENIOR ANALYTICS DASHBOARD",fontsize=17,fontweight="bold",color="green")
plt.tight_layout()
plt.savefig("Senior Management.png",dpi=300)
plt.show()

salary_management = df.groupby("Senior Management")["Salary"].mean()
print(salary_management)
plt.figure(figsize=(8,5))

plt.bar(salary_management.index,salary_management.values)

plt.title("Average Salary by Senior Management")
plt.xlabel("Senior Management")
plt.ylabel("Average Salary")
plt.grid(axis="y")
plt.show()


bonus_report = df.groupby("Team")["Bonus %"].mean()
print(bonus_report)
plt.figure(figsize=(10,6))
plt.barh(bonus_report.index,bonus_report.values,color="green")
plt.title("Average Bonus % by Team")
plt.xlabel("Average Bonus %")
plt.ylabel("Team")
plt.grid(axis="x")
plt.tight_layout()
plt.show()

max_salary = df.groupby("Team")["Salary"].max()
print(max_salary)
plt.figure(figsize=(10,6))

plt.barh(max_salary.index,max_salary.values,color="orange")
plt.title("maximum salary team")
plt.xlabel("max_salary")
plt.ylabel("Team")
plt.grid(axis="y")
plt.tight_layout()
plt.show()

min_salary = df.groupby("Team")["Salary"].min()
print(min_salary)

plt.figure(figsize=(10,6))

plt.barh(min_salary.index,min_salary.values,color="black")
plt.title("Minimum Salary by Team")
plt.xlabel("Minimum Salary")
plt.ylabel("Team")
plt.grid(axis="x")
plt.tight_layout()
plt.show


plt.figure(figsize=(10,7))
plt.hist(df["Salary"],bins=20,color="steelblue",edgecolor="black")
plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Number of Employees")
plt.xticks(rotation=45)
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()


import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("employees.csv")

# ==============================
# Joining Year Analysis
# ==============================

df["Start Date"] = pd.to_datetime(df["Start Date"])

df["Joining Year"] = df["Start Date"].dt.year

joining_report = df["Joining Year"].value_counts().sort_index()

print(joining_report)

# ==============================
# Joining Year Chart
# ==============================

plt.figure(figsize=(12,6))

plt.bar(
    joining_report.index,
    joining_report.values,
    color="steelblue",
    edgecolor="black"
)

plt.title("Employees Joining by Year")
plt.xlabel("Joining Year")
plt.ylabel("Number of Employees")

plt.grid(axis="y", linestyle="--", alpha=0.5)

plt.tight_layout()
plt.show()

plt.figure(figsize=(10,6))

plt.scatter(
    df["Salary"],
    df["Bonus %"],
    color="purple",
    alpha=0.6
)

plt.title("Salary vs Bonus %")
plt.xlabel("Salary")
plt.ylabel("Bonus %")

plt.grid(True, linestyle="--", alpha=0.5)

plt.tight_layout()

plt.show()



import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("employees.csv")

print(df.head())
print(df.columns)

team_salary = df.groupby("Team")["Salary"].sum()
print(team_salary)

gender_report = df["Gender"].value_counts()
print(gender_report)

employee_count = df["Team"].value_counts()
print(employee_count)

average_salary = df.groupby("Team")["Salary"].mean()
print(average_salary)

fig, ax = plt.subplots(3,2,figsize=(18, 15))

ax[0,0].barh(team_salary.index,team_salary.values,color="steelblue",edgecolor="black")
ax[0,0].set_title("Team Wise Total Salary",fontsize=14,fontweight="bold")

ax[0,0].set_xlabel("Total Salary")
ax[0,0].set_ylabel("Team")
ax[0,0].grid(axis="x",linestyle="--",alpha=0.5)

ax[0,1].pie(gender_report.values,labels=gender_report.index,autopct="%1.1f%%",startangle=90)
ax[0,1].set_title("Gender Distribution",fontsize=14,fontweight="bold")
ax[1,0].barh(employee_count.index,employee_count.values,color="orange",edgecolor="black")

ax[1,0].set_title("Employees Per Team",fontsize=14,fontweight="bold")
ax[1,0].set_xlabel("Number of Employees")
ax[1,0].set_ylabel("Team")
ax[1,0].grid(axis="x",linestyle="--",alpha=0.5)

ax[1,1].barh(average_salary.index,average_salary.values,color="green",edgecolor="black")
ax[1,1].set_title("Average Salary By Team",fontsize=14,fontweight="bold")
ax[1,1].set_xlabel("Average Salary")
ax[1,1].set_ylabel("Team")

ax[1,1].grid(axis="x",linestyle="--",alpha=0.5)

ax[2,0].hist(df["Salary"],bins=20,color="steelblue",edgecolor="black")
ax[2,0].set_title("Salary Distribution",fontsize=14,fontweight="bold")

ax[2,0].set_xlabel("Salary")
ax[2,0].set_ylabel("Number of Employees")
ax[2,0].grid(axis="y",linestyle="--",alpha=0.5)

ax[2,1].scatter(df["Salary"],df["Bonus %"],color="purple",alpha=0.6)
ax[2,1].set_title("Salary vs Bonus %",fontsize=14,fontweight="bold")
ax[2,1].set_xlabel("Salary")
ax[2,1].set_ylabel("Bonus %")

ax[2,1].grid(True,linestyle="--",alpha=0.5)

fig.suptitle("EMPLOYEE ANALYTICS DASHBOARD",fontsize=20,fontweight="bold",color="black")
plt.subplots_adjust(hspace=0.45,wspace=0.30,top=0.92,bottom=0.06,left=0.08,right=0.95)
plt.savefig("Employee_Analytics_Dashboard.png",dpi=300,bbox_inches="tight")
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("employees.csv")

team_salary = df.groupby("Team")["Salary"].sum()

max_team = team_salary.idxmax()
max_value = team_salary.max()

print("Highest Salary Team:", max_team)
print("Highest Total Salary:", max_value)

fig, ax = plt.subplots(figsize=(10, 6))

ax.barh(team_salary.index,team_salary.values,color="steelblue",edgecolor="black")
ax.set_title("Team Wise Total Salary",fontsize=14,fontweight="bold")
ax.set_xlabel("Total Salary")
ax.set_ylabel("Team")
ax.grid(axis="x",linestyle="--",alpha=0.5)
max_position = team_salary.index.get_loc(max_team)

ax.set_xlim(0,max_value + 1500000)
ax.annotate(f"Highest: {max_team}\n₹{max_value:,.0f}",xy=(max_value, max_position),xytext=(max_value + 300000, max_position),arrowprops=dict(arrowstyle="->",lw=1.5))
plt.tight_layout()
plt.show()


import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("employees.csv")

print(df.head())
print(df.shape)
print(df.columns)

team_salary = df.groupby("Team")["Salary"].sum()
gender_report = df["Gender"].value_counts()
employee_count = df["Team"].value_counts()
average_salary = df.groupby("Team")["Salary"].mean()
management_report = df["Senior Management"].value_counts()
salary_data = df["Salary"]
bonus_data = df["Bonus %"]

total_employees = df["First Name"].count()
average_salary_all = df["Salary"].mean()
highest_salary = df["Salary"].max()
lowest_salary = df["Salary"].min()
highest_salary_employee = df.loc[df["Salary"].idxmax(),"First Name"]
highest_salary_team = df.loc[df["Salary"].idxmax(),"Team"]

print("\n================ KPI ================")
print("Total Employees:", total_employees)
print("Average Salary:",f"₹{average_salary_all:,.0f}")
print("Highest Salary:",f"₹{highest_salary:,.0f}")
print("Lowest Salary:",f"₹{lowest_salary:,.0f}")
print("Highest Salary Employee:",highest_salary_employee)
print("Highest Salary Team:",highest_salary_team)

fig, ax = plt.subplots(3,2,figsize=(18, 15))

bars1 = ax[0,0].barh(team_salary.index,team_salary.values,color="steelblue",edgecolor="black")
ax[0,0].set_title("Team Wise Total Salary",fontsize=14,fontweight="bold")
ax[0,0].set_xlabel("Total Salary")
ax[0,0].set_ylabel("Team")
ax[0,0].grid(axis="x",linestyle="--",alpha=0.5)
ax[0,0].bar_label(bars1,fmt="%.0f",padding=3)

ax[0,1].pie(gender_report.values,labels=gender_report.index,autopct="%1.1f%%",startangle=90)
ax[0,1].set_title("Gender Distribution",fontsize=14,fontweight="bold")

bars3 = ax[1,0].barh(employee_count.index,employee_count.values,color="orange",edgecolor="black")
ax[1,0].set_title("Employees Per Team",fontsize=14,fontweight="bold")
ax[1,0].set_xlabel("Number of Employees")
ax[1,0].set_ylabel("Team")
ax[1,0].grid(axis="x",linestyle="--",alpha=0.5)
ax[1,0].bar_label(bars3,padding=3)

bars4 = ax[1,1].barh(average_salary.index,average_salary.values,color="green",edgecolor="black")
ax[1,1].set_title("Average Salary By Team",fontsize=14,fontweight="bold")
ax[1,1].set_xlabel("Average Salary")
ax[1,1].set_ylabel("Team")
ax[1,1].grid(axis="x",linestyle="--",alpha=0.5)
ax[1,1].bar_label(bars4,fmt="%.0f",padding=3)

avg_team_salary = average_salary.mean()

ax[1,1].axvline(avg_team_salary,linestyle="--",linewidth=1.5)
ax[1,1].text(avg_team_salary,9.5,f"Average: ₹{avg_team_salary:,.0f}",ha="center")

ax[2,0].hist(salary_data,bins=20,color="purple",edgecolor="black",alpha=0.75)
ax[2,0].set_title("Salary Distribution",fontsize=14,fontweight="bold")
ax[2,0].set_xlabel("Salary")
ax[2,0].set_ylabel("Number of Employees")
ax[2,0].grid(axis="y",linestyle="--",alpha=0.5)
ax[2,0].axvline(average_salary_all,linestyle="--",linewidth=2,label=f"Average ₹{average_salary_all:,.0f}")
ax[2,0].legend()

ax[2,1].scatter(salary_data,bonus_data,color="red",alpha=0.6,edgecolor="black")
ax[2,1].set_title("Salary vs Bonus %",fontsize=14,fontweight="bold")
ax[2,1].set_xlabel("Salary")
ax[2,1].set_ylabel("Bonus %")
ax[2,1].grid(True,linestyle="--",alpha=0.5)
ax[2,1].axvline(average_salary_all,linestyle="--",linewidth=1.5,label="Average Salary")
ax[2,1].legend()

fig.suptitle(
    "EMPLOYEE ANALYTICS DASHBOARD",
    fontsize=22,
    fontweight="bold",
    y=0.98
)

fig.text(
    0.20,0.925,
    f"TOTAL EMPLOYEES\n{total_employees}",
    ha="center",
    va="center",
    fontsize=13,
    fontweight="bold",
    bbox=dict(
        boxstyle="round,pad=0.6",
        edgecolor="black",
        facecolor="lightblue"
    )
)

fig.text(
    0.50,0.925,
    f"AVERAGE SALARY\n₹{average_salary_all:,.0f}",
    ha="center",
    va="center",
    fontsize=13,
    fontweight="bold",
    bbox=dict(
        boxstyle="round,pad=0.6",
        edgecolor="black",
        facecolor="lightgreen"
    )
)

fig.text(
    0.80,0.925,
    f"HIGHEST SALARY\n₹{highest_salary:,.0f}",
    ha="center",
    va="center",
    fontsize=13,
    fontweight="bold",
    bbox=dict(
        boxstyle="round,pad=0.6",
        edgecolor="black",
        facecolor="lightyellow"
    )
)

plt.subplots_adjust(
    hspace=0.55,
    wspace=0.35,
    top=0.84,
    bottom=0.06,
    left=0.10,
    right=0.95
)
plt.savefig("Employee_Analytics_Final_Dashboard.png",dpi=300,bbox_inches="tight")

plt.show()
