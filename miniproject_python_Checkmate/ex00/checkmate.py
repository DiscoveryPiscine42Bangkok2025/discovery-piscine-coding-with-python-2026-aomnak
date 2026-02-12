def checkmate(board_str):
    try:
        # Convert string -> 2D board
        rows = board_str.splitlines()
        board = [list(row) for row in rows]

        n = len(board)
        # Check square board
        for row in board:
            if len(row) != n:
                return
        # Find King
        king_row = -1
        king_col = -1
        king_count = 0

        for i in range(n):
            for j in range(n):
                if board[i][j] == 'K':
                    king_row = i
                    king_col = j
                    king_count += 1

        # Validate King count
        if king_count == 0:
            print("K < 1")
            return
        
        if king_count > 1:
            print("K > 1")
            return
        
        # Check board bounds
        def in_bounds(r, c):
            return 0 <= r < n and 0 <= c < n
        
        # Scan all pieces
        for i in range(n):
            for j in range(n):
                piece = board[i][j]

                # Pawn
                if piece == 'P':
                    for dc in [-1, 1]:
                        r = i - 1
                        c = j + dc
                        if in_bounds(r, c):
                            if r == king_row and c == king_col:
                                print("Success")
                                return

                # Rook
                if piece == 'R':
                    directions = [(1,0), (-1,0), (0,1), (0,-1)]
                    for dr, dc in directions:
                        r, c = i, j
                        while True:
                            r += dr
                            c += dc
                            if not in_bounds(r, c):
                                break
                            if r == king_row and c == king_col:
                                print("Success")
                                return

                            if board[r][c] != '.':
                                break

                # Bishop
                if piece == 'B':
                    directions = [(1,1), (1,-1), (-1,1), (-1,-1)]
                    for dr, dc in directions:
                        r, c = i, j
                        while True:
                            r += dr
                            c += dc
                            if not in_bounds(r, c):
                                break
                            if r == king_row and c == king_col:
                                print("Success")
                                return

                            if board[r][c] != '.':
                                break

                # Queen
                if piece == 'Q': # Rook + Bishop
                    directions = [
                        (1,0), (-1,0), (0,1), (0,-1),
                        (1,1), (1,-1), (-1,1), (-1,-1)
                    ]
                    for dr, dc in directions:
                        r, c = i, j
                        while True:
                            r += dr
                            c += dc
                            if not in_bounds(r, c):
                                break
                            if r == king_row and c == king_col:
                                print("Success")
                                return

                            if board[r][c] != '.':
                                break
        # No attack found
        print("Fail")

    except:
        return