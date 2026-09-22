project1 = {"Vanitha", "Vasanthi", "Subashini"}
project2 = {"Subasri", "Karkuzhali", "Praveena"}
project3 = {"Vanitha", "Naveena", "Karkuzhali"}
employee = "Vanitha"
count = 0
projects = [project1, project2, project3]
for project in projects:
    if employee in project:
        count = count + 1
print(employee, "is working in", count, "projects")
