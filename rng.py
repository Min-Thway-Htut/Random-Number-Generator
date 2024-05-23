import sys
import os
import time

# Auxiliary file to store the seed
SEED_FILE = "seed.txt"


def save_seed(seed):
    """Save the seed to an auxiliary text file."""
    with open(SEED_FILE, 'w') as f:
        f.write(str(seed))


def load_seed():
    """Load the seed from the auxiliary text file, if it exists."""
    if os.path.exists(SEED_FILE):
        with open(SEED_FILE, 'r') as f:
            return int(f.read().strip())
    return None


def generate_random_number(seed):
    """Generate a pseudo-random number using a simple linear congruential generator (LCG)."""
    # LCG parameters
    a = 1664525
    c = 1013904223
    m = 2 ** 32

    # Update seed
    new_seed = (a * seed + c) % m

    # Save the new seed
    save_seed(new_seed)

    return new_seed


def main():
    if len(sys.argv) == 1:
        # No parameter: generate a random number
        seed = load_seed()
        if seed is None:
            # If no seed is found, use the current time as the initial seed
            seed = int(time.time()) & 0xFFFFFFFF  # Ensuring seed is a 32-bit value
        random_number = generate_random_number(seed)
        print(random_number)
    elif len(sys.argv) == 3 and sys.argv[1] == '-s':
        # Parameter "-s" with a seed value
        try:
            seed = int(sys.argv[2])
            if seed < 0 or seed >= 2 ** 32:
                raise ValueError("Seed must be a 32-bit integer (0 <= seed < 2^32).")
            save_seed(seed)
            print(f"Seed set to: {seed}")
        except ValueError as e:
            print(f"Invalid seed value: {e}")
    else:
        print("Usage: python script.py [-s seed_value]")


if __name__ == "__main__":
    main()