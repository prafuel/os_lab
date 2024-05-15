def fifoPageReplacement(pages, n, capacity):
    frame = [-1] * capacity
    pageFaults = 0
    front = 0  # Pointer to the first page in the frame

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
            # Page is not present, replace the oldest page in the frame
            frame[front] = page
            front = (front + 1) % capacity
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

    fifoPageReplacement(pages, n, capacity)


if __name__ == "__main__":
    main()