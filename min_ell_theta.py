def learn_theta(data, colors):
    max_blue = None
    min_red = None

    for x, c in zip(data, colors):
        if c == 'blue':
            if max_blue is None or x > max_blue:
                max_blue = x
        elif c == 'red':
            if min_red is None or x < min_red:
                min_red = x

    return (max_blue + min_red) / 2

def compute_ell(data, colors, theta):
    loss = 0

    for x, c in zip(data, colors):
        if c == 'red' and x <= theta:
            loss += 1
        elif c == 'blue' and x > theta:
            loss += 1

    return loss

def minimize_ell(data, colors):
    pairs = sorted(zip(data, colors))

    loss = sum(1 for c in colors if c == 'blue')

    best_loss = loss
    best_theta = pairs[0][0] - 1

    for x, c in pairs:
        if c == 'blue':
            loss -= 1
        elif c == 'red':
            loss += 1

        if loss < best_loss:
            best_loss = loss
            best_theta = x

    return best_theta

def minimize_ell_sorted(data, colors):
    loss = sum(1 for c in colors if c == 'blue')

    best_loss = loss
    best_theta = data[0] - 1

    for i in range(len(data)):
        if colors[i] == 'blue':
            loss -= 1
        elif colors[i] == 'red':
            loss += 1

        if loss < best_loss:
            best_loss = loss
            best_theta = data[i]

    return best_theta