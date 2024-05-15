def lruPageReplacement(pages, n, capacity):
    frame = [-1] * capacity
    pageFaults = 0
    recentCount = 0
    recent = [0] * capacity

    print("Incoming\tFrame")
    for i in range(n):
        page = pages[i]
        pageFound = False

        # Check if the page is already present in the frame
        for j in range(capacity):
            if frame[j] == page:
                pageFound = True
                recent[j] = recentCount
                recentCount += 1
                break

        if not pageFound:
            # Page is not present, find the least recently used page in the frame
            lruIndex = recent.index(min(recent))

            # Replace the least recently used page with the new page
            frame[lruIndex] = page
            recent[lruIndex] = recentCount
            recentCount += 1
            pageFaults += 1

        # Print the current page and frame status
        print(f"{page}\t\t", end="")
        for j in range(capacity):
            if frame[j] != -1:
                print(f"{frame[j]}\t\t", end="")
            else:
                print("-\t\t", end="")
        print()

    print(f"\nTotal Page Faults: {pageFaults}")


def main():
    n = int(input("Enter the number of pages: "))
    pages = list(map(int, input("Enter the sequence of page requests:\n").split()))
    capacity = int(input("Enter the number of frames: "))

    lruPageReplacement(pages, n, capacity)


if __name__ == "_main_":
    main()