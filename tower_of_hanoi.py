#tower_of_hanoi
def tower_of_hanoi(n, source_peg, target_peg, auxiliary_peg):
    if n == 1:
        print(f"Move disk 1 from {source_peg} to {target_peg}")
        return
    tower_of_hanoi(n - 1, source_peg, auxiliary_peg, target_peg)
    print(f"Move disk {n} from {source_peg} to {target_peg}")
    tower_of_hanoi(n - 1, auxiliary_peg, target_peg, source_peg)

# Example usage:
number_of_disks = 3
source_peg, target_peg, auxiliary_peg = 'A', 'C', 'B'

print(f"Solving Tower of Hanoi for {number_of_disks} disks:")
tower_of_hanoi(number_of_disks, source_peg, target_peg, auxiliary_peg)