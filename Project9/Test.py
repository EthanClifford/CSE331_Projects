from Project9.Graph import Graph, fake_emails

stu = Graph(size=20, connectedness=0.1)

print(stu.adj_list)

fake = fake_emails(stu, mark_fake=True)


print("Your Graph structure:")
for k, v in stu.adj_list.items():
    print(k, v, [repr(e) for e in v.edges])
print("\n")
print("Your Fake: ", sorted(fake))

