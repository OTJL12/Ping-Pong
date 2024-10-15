def pingPong(player1, win):
    hits = []
    for hit in player1:
        hits.append(hit)
        if hit == "Ping!":
            hits.append("Pong!")
    if not win:
        hits.pop()
    return hits

print(pingPong(["Ping!"], True))
print(pingPong(["Ping!", "Ping!"], False))
print(pingPong(["Ping!", "Ping!", "Ping!"], True))