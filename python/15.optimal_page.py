def findOptimalPage(pages, frame, n, capacity, index):
    res = -1
    farthest = index
    for i in range(capacity):
        for j in range(index, n):
            if frame[i] == pages[j]:
                if j > farthest:
                    farthest = j
                    res = i
                break
        # If the page is not present in the future pages, return it.
        if j == n:
            return i
    return res if res != -1 else 0


def optimalPageReplacement(pages, n, capacity):
    frame = [-1] * capacity
    pageFaults = 0

    print("Incoming\tFrame")
    for i in range(n):
        page = pages[i]
        pageFound = False

        # Check if the page is already present in the frame
        for j in range(capacity):
            if frame[j] == page:
                pageFound = True
                break

        if not pageFound:
            replaceIndex = findOptimalPage(pages, frame, n, capacity, i)
            frame[replaceIndex] = page
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

    optimalPageReplacement(pages, n, capacity)


if __name__ == "__main__":
    main()