def decode(message_file):
    def generate_sequence(n):
        """
        Generate the sequence based on the formula: n * (n + 1) / 2
        """
        sequence = [int(i * (i + 1) / 2) for i in range(1, n + 1)]
        return sequence
    pyramid = {}

    with open(message_file, 'r') as file:
        for line in file:
            number, word = line.strip().split(' ')
            pyramid[int(number)] = word

    output = []

    for i in generate_sequence(len(pyramid.items())):
        output.append(pyramid.get(i, ""))

    print(" ".join(output).strip())


decode("test.txt")
