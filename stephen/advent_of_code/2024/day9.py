"""
--- Day 9: Disk Fragmenter ---
Another push of the button leaves you in the familiar hallways of some friendly amphipods!
Good thing you each somehow got your own personal mini submarine. 
The Historians jet away in search of the Chief, mostly by driving directly into walls.

While The Historians quickly figure out how to pilot these things,
you notice an amphipod in the corner struggling with his computer.
 He's trying to make more contiguous free space by compacting all of the files, but his program isn't working; 
you offer to help.

He shows you the disk map (your puzzle input) he's already generated. For example:

2333133121414131402
The disk map uses a dense format to represent the layout of files and free space on the disk.
 The digits alternate between indicating the length of a file and the length of free space.

So, a disk map like 12345 would represent a one-block file,
 two blocks of free space, a three-block file, four blocks of free space, 
 and then a five-block file.
A disk map like 90909 would represent three nine-block files in a row (with no free space between them).

Each file on disk also has an ID number based on the order of the
 files as they appear before they are rearranged,
starting with ID 0. So, the disk map 12345 has three files:
 a one-block file with ID 0, a three-block file with ID 1,
   and a five-block file with ID 2. Using one character for each block where digits are the file ID and . is free space, the disk map 12345 represents these individual blocks:

0..111....22222
The first example above, 2333133121414131402, represents these individual blocks:

00...111...2...333.44.5555.6666.777.888899
The amphipod would like to move file blocks one at a time from the end of the disk to the leftmost free space
 block (until there are no gaps remaining between file blocks). For the disk map 12345, the process looks like this:

0..111....22222
02.111....2222.
022111....222..
0221112...22...
02211122..2....
022111222......
The first example requires a few more steps:

00...111...2...333.44.5555.6666.777.888899
009..111...2...333.44.5555.6666.777.88889.
0099.111...2...333.44.5555.6666.777.8888..
00998111...2...333.44.5555.6666.777.888...
009981118..2...333.44.5555.6666.777.88....
0099811188.2...333.44.5555.6666.777.8.....
009981118882...333.44.5555.6666.777.......
0099811188827..333.44.5555.6666.77........
00998111888277.333.44.5555.6666.7.........
009981118882777333.44.5555.6666...........
009981118882777333644.5555.666............
00998111888277733364465555.66.............
0099811188827773336446555566..............
The final step of this file-compacting process is to update the filesystem checksum. To calculate the checksum, add up the result of multiplying each of these blocks' position with the file ID number it contains. The leftmost block is in position 0. If a block contains free space, skip it instead.

Continuing the first example, the first few blocks' position multiplied by its file ID number are 0 * 0 = 0, 1 * 0 = 0, 2 * 9 = 18, 3 * 9 = 27, 4 * 8 = 32, and so on. In this example, the checksum is the sum of these, 1928.

Compact the amphipod's hard drive using the process he requested. What is the resulting filesystem checksum? (Be careful copy/pasting the input for this puzzle; it is a single, very long line.)


"""


def calculate_checksum(disk_map):
    # Parse the disk map into file and space segments
    segments = []
    is_file = True
    for digit in disk_map:
        length = int(digit)
        segments.append((length, is_file))
        is_file = not is_file

    # Build the initial disk blocks with file IDs and free spaces
    disk_blocks = []
    file_id = 0
    for length, is_file in segments:
        if is_file:
            disk_blocks.extend([file_id] * length)
            file_id += 1
        else:
            disk_blocks.extend(["."] * length)

    # Simulate the compaction process
    while True:
        try:
            free_index = disk_blocks.index(".")
        except ValueError:
            break  # No free space left

        # Find the rightmost file block
        file_index = None
        for i in range(len(disk_blocks) - 1, -1, -1):
            if disk_blocks[i] != ".":
                file_index = i
                break

        if file_index is None or file_index < free_index:
            break  # No file blocks to move

        # Move the file block to the leftmost free space
        disk_blocks[free_index] = disk_blocks[file_index]
        disk_blocks[file_index] = "."

    # Calculate the checksum
    checksum = sum(
        position * int(block)
        for position, block in enumerate(disk_blocks)
        if block != "."
    )

    return checksum


# Replace 'disk_map_input' with your actual puzzle input (a single, very long line of digits)
disk_map_input = open("input9.txt", encoding="utf-8").read().strip()

# checksum = calculate_checksum(disk_map_input)
# print(f"The resulting filesystem checksum is: {checksum}")

# --- Part Two ---
"""
Compacting the amphipod's hard drive was a success! You've earned the amphipod's trust and gratitude.

This time, attempt to move whole files to the leftmost span of free space blocks
 that could fit the file. Attempt to move each file exactly once in order of decreasing
file ID number starting with the file with the highest file ID number. If there is no span of free space to
     the left of a file that is large enough to fit the file, the file does not move.

The first example from above now proceeds differently:

00...111...2...333.44.5555.6666.777.888899
0099.111...2...333.44.5555.6666.777.8888..
0099.1117772...333.44.5555.6666.....8888..
0099.111777244.333....5555.6666.....8888..
00992111777.44.333....5555.6666.....8888..
The process of updating the filesystem checksum is the same; now, this example's checksum would be 2858.

Start over, now compacting the amphipod's hard drive using this new method instead. What is the resulting filesystem checksum?
"""


def calculate_checksum_v2(disk_map):
    # Parse the disk map into file and space segments
    segments = []
    is_file = True
    for digit in disk_map:
        length = int(digit)
        segments.append((length, is_file))
        is_file = not is_file

    # Build the initial disk blocks with file IDs and free spaces
    disk_blocks = []
    file_id = 0
    for length, is_file in segments:
        if is_file:
            disk_blocks.extend([file_id] * length)
            file_id += 1
        else:
            disk_blocks.extend(["."] * length)

    # Simulate the new compaction process
    for current_file_id in range(file_id - 1, -1, -1):
        # Find the current file blocks
        file_blocks = [
            i for i, block in enumerate(disk_blocks) if block == current_file_id
        ]
        if not file_blocks:
            continue

        leftmost_block = min(file_blocks)
        file_length = len(file_blocks)

        # Find the leftmost span of free space that can fit the file
        suitable_span_found = False
        for i in range(leftmost_block - file_length + 1):
            if all(block == "." for block in disk_blocks[i : i + file_length]):
                # Move the file to this span of free space
                for j in range(file_length):
                    disk_blocks[i + j] = current_file_id
                for j in file_blocks:
                    disk_blocks[j] = "."
                suitable_span_found = True
                break

        if not suitable_span_found:
            # If no suitable span is found, the file does not move
            continue

    # Calculate the checksum
    checksum = sum(
        position * block for position, block in enumerate(disk_blocks) if block != "."
    )

    return checksum


# checksum_v2 = calculate_checksum_v2(disk_map_input)
# print(f"The resulting filesystem checksum for part two is: {checksum_v2}")


def solve3(disk_map):
    cur_id = 0
    id_to_length = dict()
    row = []
    for idx, val in enumerate(disk_map):
        if idx % 2 == 1:
            row.extend(["."] * int(val))
        else:
            row.extend([cur_id] * int(val))
            id_to_length[cur_id] = int(val)
            cur_id += 1
    file_ids = sorted(list(id_to_length.keys()))
    while file_ids:
        cur_id = file_ids.pop()
        start_idx = row.index(cur_id)
        can_move = False
        for i in range(0, start_idx):
            if row[i] == ".":
                can_move = True
        if not can_move:
            break
        cur_length = id_to_length[cur_id]
        for idx, val in enumerate(row):
            if row[idx] == cur_id:
                break
            if idx + cur_length >= len(row):
                break
            if val == "." and all(x == "." for x in row[idx : idx + cur_length]):
                for i in range(cur_length):
                    row[idx + i] = cur_id
                for i in range(idx + cur_length, len(row)):
                    if row[i] == cur_id:
                        row[i] = "."
                break
    check_sum = 0
    for idx, val in enumerate(row):
        if val == ".":
            continue
        check_sum += idx * val
    print(check_sum)


disk_map_input = open("input9.txt", encoding="utf-8").read().strip()
solve3(disk_map_input)
